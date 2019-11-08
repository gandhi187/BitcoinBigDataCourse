
function splitDAO(
  uint _proposalID,
  address _newCurator
) noEther onlyTokenholders returns (bool _success) {
  ...
  // [Added for explanation] The first step moves Ether and assigns new tokens
  uint fundsToBeMoved =
      (balances[msg.sender] * p.splitData[0].splitBalance) /
      p.splitData[0].totalSupply;
  if (p.splitData[0].newDAO.createTokenProxy.value(fundsToBeMoved)(msg.sender) == false) // [Added for explanation] This is the line that splits the DAO before updating the funds in the account calling for the split
  ...
  // Burn DAO Tokens
  Transfer(msg.sender, 0, balances[msg.sender]);
  withdrawRewardFor(msg.sender); // be nice, and get his rewards
  // [Added for explanation] The previous line is key in that it is called before totalSupply and balances[msg.sender] are updated to reflect the new balances after the split has been performed
  totalSupply -= balances[msg.sender]; // [Added for explanation] This happens after the split
  balances[msg.sender] = 0; // [Added for explanation] This also happens after the split
  paidOut[msg.sender] = 0;
  return true;
}
