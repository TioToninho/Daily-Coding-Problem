fn soma_k(nums: &[i32], k: i32) -> bool {
  for num in nums {
    if nums.contains(&(k - num)) {
      return true;
    }
  }
  false
}


println!("{}", soma_k(&[10, 15, 3, 7], 17));
