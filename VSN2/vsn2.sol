pragma solidity >=0.4.22 <0.6.0;

contract write {
    mapping(bytes32 => bytes32) public I; 
    mapping(bytes32 => bytes) public AL; 
    bytes32 [] public  R ;
    int256 [] public  M ;
    uint c = 0;
    bytes pp = hex'000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001';


    function expmod(bytes memory g, uint256 x, bytes memory p) public view returns ( bytes memory) {
        require(p.length == 384,"unqualified length of p");
        require(g.length == 384,"unqualified length of g");
        bytes memory input = abi.encodePacked(bytes32(g.length),abi.encode(0x20),bytes32(p.length),g,bytes32(x),p);
        bytes memory result = new bytes(384);
        bytes memory pointer = new bytes(384);
        assembly {
            if iszero(staticcall(sub(gas, 2000), 0x05, add(input,0x20), 0x380, add(pointer,0x20), 0x180 )) {
                revert(0, 0)
            }
        }
        for(uint i =0; i<12;i++) {
            bytes32 value;
            uint256 start = 32*i;
            assembly {
                value := mload(add(add(pointer,0x20),start))
            }
            for(uint j=0;j<32;j++) {
                result[start+j] = value[j];
            }
        }
        return result;
    }
   

    //传入EDB里值的函数
    function set_I(bytes32 add, bytes32 val) public{
        I[add]=val;
    } 

    function set_AL(bytes32 add, bytes memory val) public{
        AL[add]=val;
    } 

    function search(bytes32 G_u_1,uint256 tk) public {
        
        bytes memory AI = new bytes(384);
        AI = AL[G_u_1];
        bytes  memory T = expmod(AI,tk,pp);

        bytes32 t = keccak256(abi.encodePacked(T));
        if(I[t] != bytes32(0x0)){
            M.push(1);
            bytes32 st_0 =  I[t] ^ keccak256(abi.encodePacked(T));
            
            bytes32 l = keccak256(abi.encodePacked(st_0));
            while(I[l] != bytes32(0x0)){
                M.push(2);
                bytes32 temp = I[l] ^ keccak256(abi.encodePacked(st_0)); 
                bytes memory st = new bytes(32);
                for(uint j = 0;j < 16;j++){//进行赋值
                    st[j] = 0;
                }
                for(uint j = 16;j < 32;j++){//进行赋值
                    st[j] = temp[j];
                }
                R.push(temp);
                l = keccak256(abi.encodePacked(st));
            }
        }
    }

   
    function retrieve0() public view returns(bytes32 [] memory){
        return R;
    }
    function retrieve1() public view returns(uint256){
        return R.length;
    }
    function retrieve2() public view returns(int256 [] memory){
        return M;
    }

    

}