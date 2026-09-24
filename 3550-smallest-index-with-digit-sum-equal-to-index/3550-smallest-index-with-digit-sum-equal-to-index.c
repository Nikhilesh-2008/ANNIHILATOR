int smallestIndex(int* nums, int numsSize) {
    for(int i=0;i<numsSize;i++){
        int x=nums[i];
        int s=0;
        while(x>0){
            int d=x%10;
            s+=d;
            x/=10;
        }
        if(i==s){
            return i;
        }
    }
    return -1;
}