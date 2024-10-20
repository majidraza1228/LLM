pip install torch
pip install -U transformers sentencepiece accelerate sentence transformers
pip install protobuf
pip install einops


nvidia-smi


https://github.com/itsPreto

https://gist.github.com/itsPreto/038abe634dd10e9850768cd0b13ed169



Pytorch and Coda
=================

conda create -n dolphin python=3.11

conda create -n nemo python=3.11 -y & conda activate nemo

conda install -c nvidia  cuda-nvcc
conda install -c anaconda cudatoolkit
conda install pytorch torchvision torchaudio pytorch-cuda -c pytorch -c nvidia



curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3:70b-instruct
ollama pull llama3:instruct

https://github.com/Doriandarko/maestro



python3 -m graphrag.index --init --root ./ragtest
pip install  graphrag
conda create -n graphollama python=3.11 -y  && conda activate graphollama
ollama pull  nomic-embed-text
ollama pull  mistral

pip install torch 

pip install git+https://github.com/huggingface/transformers
pip install git+https://github.com/huggingface/accelerate

pip install huggingface_hub


pip install datasets dataclasses
conda install jupyter -y
pip uninstall charset_normalizer -y
pip install charset_normalizer
jupyter notebook




pip install datasets dataclasses


pip install torch
pip install git+https://github.com/huggingface/transformers
pip install git+https://github.com/huggingface/acceleratene-
pip install accelerate openai
pip  install nemo-agent


pip install llama-index
pip install llama-index-core
pip install llama-parse

https://github.com/truemagic-coder/nemo-agent


ollama pull mistral-nemo

conda install jupyter -y
pip uninstall charset_normalizer -y
pip install charset_normalizer
jupyter notebook



-------------------------------------------------------   Install Node ----------------------------------------------

To install NVM (Node Version Manager) and Node.js on Ubuntu, follow these steps:

1. **Update your system**:
   ```bash
   sudo apt update
   ```

2. **Install NVM**:
   Use the following command to download and install NVM:
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
   ```

3. **Load NVM**:
   After installation, you need to load NVM. Add the following lines to your `.bashrc` or `.zshrc` file:
   ```bash
   export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
   ```

4. **Source the profile**:
   Apply the changes by running:
   ```bash
   source ~/.bashrc
   ```

5. **Verify NVM installation**:
   Check if NVM is installed correctly:
   ```bash
   nvm --version
   ```

6. **Install Node.js**:
   You can now install the latest version of Node.js:
   ```bash
   nvm install node
   ```
   Or install a specific version:
   ```bash
   nvm install <version>
   ```

7. **Set default Node.js version**:
   Set a default Node.js version to use:
   ```bash
   nvm alias default <version>
   ```

8. **Verify Node.js installation**:
   Check the installed Node.js version:
   ```bash
   node -v
   ```

