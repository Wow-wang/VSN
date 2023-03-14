pragma solidity >=0.4.22 <0.6.0;

contract write {
    mapping(bytes32 => bytes32) public I; 
    mapping(bytes32 => bytes ) public AL; 
    bytes32 [] public  R ;
    int256 [] public  M ;
    bytes public result1;
    bytes public pp = '0x90066455b5cfc38f9caa4a48b4281f292c260feef01fd61037e56258a7795a1c7ad46076982ce6bb956936c6ab4dcfe05e6784586940ca544b9b2140e1eb523f009d20a7e7880e4e5bfa690f1b9004a27811cd9904af70420eefd6ea11ef7da129f58835ff56b89faa637bc9ac2efaab903402229f491d8d3485261cd068699b6ba58a1ddbbef6db51e8fe34e8a78e542d7ba351c21ea8d8f1d29f5d5d15939487e27f4416b0ca632c59efd1b1eb66511a5a0fbf615b766c5862d0bd8a3fe7a0e0da0fb2fe1fcb19e8f9996a8ea0fccde538175238fc8b0ee6f29af7f642773ebe8cd5402415a01451a840476b2fceb0e388d30d4b376c37fe401c2a2c2f941dad179c540c1c8ce030d460c4d983be9ab0b20f69144c1ae13f9383ea1c08504fb0bf321503efe43488310dd8dc77ec5b8349b8bfe97c2c560ea878de87c11e3d597f1fea742d73eec7f37be43949ef1a0d15c3f3e3fc0a8335617055ac91328ec22b50fc15b941d3d1624cd88bc25f3e941fddc6200689581bfec416b4b2cb73';

    // function setP(bytes memory p) public{
    //     pp=p;
    // }

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

    function set_AL(bytes32 add, bytes  memory val) public{
        AL[add]=val;
    } 

    function search(bytes32 G_u_1,uint256 tk) public {
        bytes memory AI;
        AI = AL[G_u_1];
        result1 = AI;
        bytes  memory T = expmod(AI,tk,pp);
        // result1 = AI;
        // bytes32 t = keccak256(abi.encodePacked(T));
        // if(I[t] != bytes32(0x0)){
        //     M.push(1);
        //     bytes32 st_0 =  I[t] ^ keccak256(abi.encodePacked(T));
            
        //     bytes32 l = keccak256(abi.encodePacked(st_0));
        //     if(I[l] != bytes32(0x0)){
        //         M.push(2);
        //         bytes32 temp = I[l] ^ keccak256(abi.encodePacked(st_0)); 
        //         bytes memory st = new bytes(32);
        //         for(uint j = 0;j < 16;j++){//进行赋值
        //             st[j] = 0x00;
        //         }
        //         for(uint j = 16;j < 32;j++){//进行赋值
        //             st[j] = temp[j];
        //         }
        //         R.push(temp);
        //         l = keccak256(abi.encodePacked(st));
        //     }
        // }
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
    function retrieve3() public view returns(bytes memory){
        return result1;
    }

    

}



0x36743e8a55aae5af0640077eb9228dbdd62ae3b8682007b4349d8fa4ecf91717


0x36743e8a55aae5af0640077eb9228dbdd62ae3b8682007b4349d8fa4ecf91717

