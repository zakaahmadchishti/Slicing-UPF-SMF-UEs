# Open5GS with Docker Implementation

- This guide includes all the steps required to configure and put the Open5GS emulation into operation using Docker.

## Contents/Steps:

### 1. VirtualBox & Ubuntu Installation

- Install VirtualBox from the official website: [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
- Download the Ubuntu ISO image: [Ubuntu 22.04.3 LTS](https://ubuntu.com/download/desktop).

#### Steps to Set Up the Virtual Machine:

1. Open VirtualBox and create a new virtual machine (VM).
2. Load the Ubuntu ISO image as the optical disk for installation.
3. Configure the VM settings, including:
   - **Memory (RAM):** Allocate at least 4 GB (recommended for smoother operation).
   - **CPU:** Assign 2 or more processor cores.
   - **Storage:** Provide a minimum of 20 GB.
4. Start the VM and proceed with the Ubuntu installation.
   - Opt for a **minimal installation** to save resources.
5. Complete the installation by following the on-screen instructions.

### 2. Docker Installation

#### Install Docker Desktop on Ubuntu:

1. Update the package list to ensure all packages are up-to-date:
   ```sh
   sudo apt-get update
   ```
2. Download and install Docker Desktop using the following command:
   ```sh
   sudo apt-get install ./docker-desktop-amd64.deb
   ```

   - By default, Docker Desktop is installed at `/opt/docker-desktop`.

### Launch Docker Desktop:

#### GUI Method:

1. Open the **Applications** menu on your desktop.
2. Search for and select **Docker Desktop**.
3. Review the **Docker Subscription Service Agreement**.
4. Click **Accept** to continue.
   - Note: Docker Desktop will not start unless you accept the terms. If you prefer, you can accept these terms later by reopening Docker Desktop.

#### Terminal Method:

- Start Docker Desktop with the following command:
  ```sh
  systemctl --user start docker-desktop
  ```

- To enable Docker Desktop to start automatically upon sign-in:
  ```sh
  systemctl --user enable docker-desktop
  ```

### Upgrade Docker Desktop:

When a new version of Docker Desktop is released, you’ll see a notification in the Docker UI. To upgrade:

1. Download the updated package.
2. Install it using:
   ```sh
   sudo apt-get install ./docker-desktop-<arch>.deb
   ```

### Signing In with Docker Desktop for Linux:

To securely manage private images, you can initialize **pass** using a GPG key:

1. Generate a GPG key:
   ```sh
   gpg --generate-key
   ```
2. Initialize **pass** with the generated public key:
   ```sh
   pass init <your_generated_gpg-id_public_key>
   ```
3. Example output after initialization:
   ```
   mkdir: created directory '/home/user/.password-store/'
   Password store initialized for <generated_gpg-id_public_key>
   ```
4. You can now securely pull private images. When credentials are accessed, you may be prompted for the GPG password.

### 3. Cloning a Repository

#### Steps to Clone a Repository:

1. Open the terminal.
2. Navigate to the directory where you want to clone the repository.
3. Use the `git clone` command with the repository URL:
   ```sh
   git clone https://github.com/Borjis131/docker-open5gs.git
   ```
4. Example output:
   ```
   $ git clone https://github.com/Borjis131/docker-open5gs.git
   Cloning into `docker-open5gs`...
   remote: Counting objects: 10, done.
   remote: Compressing objects: 100% (8/8), done.
   remote: Total 10 (delta 1), reused 10 (delta 1)
   Unpacking objects: 100% (10/10), done.
   ```

### 4. Running a Web UI with Docker

#### Steps to Start the Web Interface:

1. Navigate to the directory containing the `docker-compose.yaml` file:
   ```sh
   cd compose-files/metrics
   ```
2. Run the following command to start the web interface:
   ```sh
   docker compose -f docker-compose.yaml --env-file=.env up -d
   ```

#### Accessing the Web Interface:

- Open your browser and navigate to:
  ```
  http://localhost:9999
  ```

#### Web UI Login Credentials:

- **Username:** admin  
- **Password:** 1423

### 5. Troubleshooting

#### 1. How to Remove a Package:

- List installed packages matching a partial name:
  ```sh
  dpkg --list | grep partial_package_name*
  ```
- Remove the package:
  ```sh
  sudo apt-get remove package_name
  ```
- Purge the package and its configuration files:
  ```sh
  sudo apt-get purge package_name
  ```
- Remove unnecessary dependencies:
  ```sh
  sudo apt-get autoremove
  ```
- Clear cached packages:
  ```sh
  sudo apt-get autoclean
  ```
- Verify the package is removed:
  ```sh
  dpkg --list | grep partial_package_name*
  ```

#### 2. Errors While Building UERANSIM:

**Error Message:**
```console
rm -fr logs # Old version log files
mkdir -p build
rm -fr build/*
CMake Error: The source directory "/home/mimo/UERANSIM-3.0.1/cmake-build-release" does not exist.
Specify --help for usage, or press the help button on the CMake GUI.
makefile:5: recipe for target 'build' failed
```

#### Solution:

1. Remove existing versions of CMake:
   ```sh
   sudo apt remove cmake
   sudo snap remove cmake
   ```
2. Reinstall CMake using the **classic** option:
   ```sh
   snap install cmake --classic
   ```
3. Retry the build process, and it should work as expected.

---


### For Virtual machine:

   1) Turn off the virtual machine and close VirtualBox.
   2) On your host (the main PC where the VM is installed), open System Control. Go to Programs and Features/   Enable or Disable Windows Features.
   3) Disable Hyper-V entirely. Also, disable Windows Hypervisor Platform and Windows Sandbox. The functions for which you needed a sandbox can usually also be performed in a VirtualBox.

 
 ### Public Website Sources.
 
 1) https://docs.docker.com/desktop/setup/install/linux/ubuntu/
    
 2) https://docs.docker.com/desktop/setup/sign-in/
    
 3) https://open5gs.org/open5gs/docs/guide/01-quickstart/

 4) https://github.com/Borjis131/docker-open5gs.git

 5) https://github.com/aligungr/UERANSIM




This detailed guide should help you seamlessly set up and manage Open5GS with Docker. Feel free to reach out if you encounter any issues!

