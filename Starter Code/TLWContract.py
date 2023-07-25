{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Python-dotenv could not parse statement starting at line 14\n",
      "Python-dotenv could not parse statement starting at line 15\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'solc'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 55\u001b[0m\n\u001b[1;32m     17\u001b[0m contract_source_code \u001b[39m=\u001b[39m \u001b[39m'''\u001b[39m\n\u001b[1;32m     18\u001b[0m \u001b[39mpragma solidity ^0.5.0;\u001b[39m\n\u001b[1;32m     19\u001b[0m \n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     51\u001b[0m \u001b[39m}\u001b[39m\n\u001b[1;32m     52\u001b[0m \u001b[39m'''\u001b[39m\n\u001b[1;32m     54\u001b[0m \u001b[39m# Compile the contract\u001b[39;00m\n\u001b[0;32m---> 55\u001b[0m compiled_sol \u001b[39m=\u001b[39m compile_source(contract_source_code)\n\u001b[1;32m     56\u001b[0m contract_interface \u001b[39m=\u001b[39m compiled_sol[\u001b[39m'\u001b[39m\u001b[39m<stdin>:TimeLockWallet\u001b[39m\u001b[39m'\u001b[39m]\n\u001b[1;32m     58\u001b[0m \u001b[39m# Get the contract ABI\u001b[39;00m\n",
      "File \u001b[0;32m~/opt/anaconda3/envs/myenv/lib/python3.8/site-packages/solc/main.py:108\u001b[0m, in \u001b[0;36mcompile_source\u001b[0;34m(source, allow_empty, output_values, **kwargs)\u001b[0m\n\u001b[1;32m    105\u001b[0m combined_json \u001b[39m=\u001b[39m \u001b[39m'\u001b[39m\u001b[39m,\u001b[39m\u001b[39m'\u001b[39m\u001b[39m.\u001b[39mjoin(output_values)\n\u001b[1;32m    106\u001b[0m compiler_kwargs \u001b[39m=\u001b[39m \u001b[39mdict\u001b[39m(stdin\u001b[39m=\u001b[39msource, combined_json\u001b[39m=\u001b[39mcombined_json, \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs)\n\u001b[0;32m--> 108\u001b[0m stdoutdata, stderrdata, command, proc \u001b[39m=\u001b[39m solc_wrapper(\u001b[39m*\u001b[39;49m\u001b[39m*\u001b[39;49mcompiler_kwargs)\n\u001b[1;32m    110\u001b[0m contracts \u001b[39m=\u001b[39m _parse_compiler_output(stdoutdata)\n\u001b[1;32m    112\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m contracts \u001b[39mand\u001b[39;00m \u001b[39mnot\u001b[39;00m allow_empty:\n",
      "File \u001b[0;32m~/opt/anaconda3/envs/myenv/lib/python3.8/site-packages/solc/utils/string.py:85\u001b[0m, in \u001b[0;36mcoerce_return_to_text.<locals>.inner\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m     83\u001b[0m \u001b[39m@functools\u001b[39m\u001b[39m.\u001b[39mwraps(fn)\n\u001b[1;32m     84\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39minner\u001b[39m(\u001b[39m*\u001b[39margs, \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs):\n\u001b[0;32m---> 85\u001b[0m     \u001b[39mreturn\u001b[39;00m force_obj_to_text(fn(\u001b[39m*\u001b[39;49margs, \u001b[39m*\u001b[39;49m\u001b[39m*\u001b[39;49mkwargs))\n",
      "File \u001b[0;32m~/opt/anaconda3/envs/myenv/lib/python3.8/site-packages/solc/wrapper.py:156\u001b[0m, in \u001b[0;36msolc_wrapper\u001b[0;34m(solc_binary, stdin, help, version, add_std, combined_json, optimize, optimize_runs, libraries, output_dir, gas, assemble, link, source_files, import_remappings, ast, ast_json, asm, asm_json, opcodes, bin, bin_runtime, clone_bin, abi, interface, hashes, userdoc, devdoc, formal, allow_paths, standard_json, success_return_code, evm_version)\u001b[0m\n\u001b[1;32m    153\u001b[0m \u001b[39mif\u001b[39;00m evm_version:\n\u001b[1;32m    154\u001b[0m     command\u001b[39m.\u001b[39mextend((\u001b[39m'\u001b[39m\u001b[39m--evm-version\u001b[39m\u001b[39m'\u001b[39m, evm_version))\n\u001b[0;32m--> 156\u001b[0m proc \u001b[39m=\u001b[39m subprocess\u001b[39m.\u001b[39;49mPopen(command,\n\u001b[1;32m    157\u001b[0m                         stdin\u001b[39m=\u001b[39;49msubprocess\u001b[39m.\u001b[39;49mPIPE,\n\u001b[1;32m    158\u001b[0m                         stdout\u001b[39m=\u001b[39;49msubprocess\u001b[39m.\u001b[39;49mPIPE,\n\u001b[1;32m    159\u001b[0m                         stderr\u001b[39m=\u001b[39;49msubprocess\u001b[39m.\u001b[39;49mPIPE)\n\u001b[1;32m    161\u001b[0m stdoutdata, stderrdata \u001b[39m=\u001b[39m proc\u001b[39m.\u001b[39mcommunicate(stdin)\n\u001b[1;32m    163\u001b[0m \u001b[39mif\u001b[39;00m proc\u001b[39m.\u001b[39mreturncode \u001b[39m!=\u001b[39m success_return_code:\n",
      "File \u001b[0;32m~/opt/anaconda3/envs/myenv/lib/python3.8/subprocess.py:858\u001b[0m, in \u001b[0;36mPopen.__init__\u001b[0;34m(self, args, bufsize, executable, stdin, stdout, stderr, preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags, restore_signals, start_new_session, pass_fds, encoding, errors, text)\u001b[0m\n\u001b[1;32m    854\u001b[0m         \u001b[39mif\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mtext_mode:\n\u001b[1;32m    855\u001b[0m             \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstderr \u001b[39m=\u001b[39m io\u001b[39m.\u001b[39mTextIOWrapper(\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstderr,\n\u001b[1;32m    856\u001b[0m                     encoding\u001b[39m=\u001b[39mencoding, errors\u001b[39m=\u001b[39merrors)\n\u001b[0;32m--> 858\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_execute_child(args, executable, preexec_fn, close_fds,\n\u001b[1;32m    859\u001b[0m                         pass_fds, cwd, env,\n\u001b[1;32m    860\u001b[0m                         startupinfo, creationflags, shell,\n\u001b[1;32m    861\u001b[0m                         p2cread, p2cwrite,\n\u001b[1;32m    862\u001b[0m                         c2pread, c2pwrite,\n\u001b[1;32m    863\u001b[0m                         errread, errwrite,\n\u001b[1;32m    864\u001b[0m                         restore_signals, start_new_session)\n\u001b[1;32m    865\u001b[0m \u001b[39mexcept\u001b[39;00m:\n\u001b[1;32m    866\u001b[0m     \u001b[39m# Cleanup if the child failed starting.\u001b[39;00m\n\u001b[1;32m    867\u001b[0m     \u001b[39mfor\u001b[39;00m f \u001b[39min\u001b[39;00m \u001b[39mfilter\u001b[39m(\u001b[39mNone\u001b[39;00m, (\u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstdin, \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstdout, \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstderr)):\n",
      "File \u001b[0;32m~/opt/anaconda3/envs/myenv/lib/python3.8/subprocess.py:1720\u001b[0m, in \u001b[0;36mPopen._execute_child\u001b[0;34m(self, args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, restore_signals, start_new_session)\u001b[0m\n\u001b[1;32m   1718\u001b[0m     \u001b[39mif\u001b[39;00m errno_num \u001b[39m!=\u001b[39m \u001b[39m0\u001b[39m:\n\u001b[1;32m   1719\u001b[0m         err_msg \u001b[39m=\u001b[39m os\u001b[39m.\u001b[39mstrerror(errno_num)\n\u001b[0;32m-> 1720\u001b[0m     \u001b[39mraise\u001b[39;00m child_exception_type(errno_num, err_msg, err_filename)\n\u001b[1;32m   1721\u001b[0m \u001b[39mraise\u001b[39;00m child_exception_type(err_msg)\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'solc'"
     ]
    }
   ],
   "source": [
    "pragma solidity ^0.5.0;\n",
    "\n",
    "contract TimeLockWallet {\n",
    "    address payable public owner;\n",
    "    uint public lockTime;\n",
    "\n",
    "    constructor() public {\n",
    "        owner = msg.sender;\n",
    "    }\n",
    "\n",
    "    function deposit() public payable {\n",
    "        require(msg.value > 0, \"Must send some ether\");\n",
    "    }\n",
    "\n",
    "    function setLockTime(uint _lockTime) public {\n",
    "        // Only allow setting the lock time when the wallet is created or when it's empty\n",
    "        require(address(this).balance == 0, \"Wallet must be empty to set the lock time\");\n",
    "        lockTime = _lockTime;\n",
    "    }\n",
    "\n",
    "    function withdraw() public {\n",
    "        require(msg.sender == owner, \"Only the owner can withdraw\");\n",
    "        require(now > lockTime, \"Wallet is locked\");\n",
    "\n",
    "        uint amount = address(this).balance;\n",
    "        (bool success, ) = owner.call.value(amount)(\"\");\n",
    "        require(success, \"Transfer failed.\");\n",
    "    }\n",
    "\n",
    "    function() external payable {\n",
    "        deposit();\n",
    "    }\n",
    "}\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "myenv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.17"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
