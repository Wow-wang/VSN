pragma solidity >=0.4.22 <0.6.0;

contract write {
    mapping(bytes32 => bytes32) public edb; 
    bytes32 []  public mei;
    bytes32 []  public st;
    uint c = 0;

    //bytes32 mei = bytes32(0x0);
    bytes32 st_1;
    bytes32 add_st;//测试bug用
    bytes32 val_tw;//测试bug用

    //传入EDB里值的函数
    function set_edb(bytes32 add, bytes32 val) public{
        edb[add]=val;
    } 

    function set_st(bytes32 val) public{
        st.push(val);
        c++;
    } 

    //
    function search(bytes32 tw) public {
        uint i = c-1;
        bytes32 add_tw = keccak256(abi.encodePacked(tw));//引入保持时间一致 
        add_tw = tw;
        val_tw = edb[add_tw];
        st_1 =  val_tw ^ add_tw;
        add_st = keccak256(abi.encodePacked(st_1));
        while(edb[add_st] != bytes32(0x0)){//如何判断mapping为空
            bytes32 val_st = edb[add_st];
            bytes32 mk = val_st ^ keccak256(abi.encodePacked(st_1));//mk 为 1||k 
            bytes32 add_ind = keccak256(abi.encodePacked(st_1));
            bytes32 val_ind = edb[add_ind];
            bytes32 EI = val_ind ^ keccak256(abi.encodePacked(st_1));
            mei.push(EI);
            if(i==0){
                break;
            }else{
                st_1 = st[i-1];
                add_st = keccak256(abi.encodePacked(st_1));
                i--;
            }
        }

        

    }
    function retrieve0() public view returns(bytes32 [] memory){
        return mei;
    }

    function retrieve1() public view returns(bytes32 [] memory){//测bug用
        return st;
    }

    // function retrieve1() public view returns(bytes32 ){
    //     return st_1;
    // }
    // function retrieve2() public view returns(bytes32 ){
    //     return val_tw;
    // }

}