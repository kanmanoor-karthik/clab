# Hey Dear friends 👋


### 😃 Hi there.
This is the basic version of the terminal based messaging server. Where anyone can host, any one can join any one. This mini project is made by myself... 
> This page contains python script, which has two files.  
>   1. **server.py** 🖥️ \
>      The main file, hosts a system as a messaging server  
>
>   2. **client.py** 💻 \
>      This is the file Where clients/ users can connect to your server.

---

### Worried about running scripts...? 😅

Dead simple... ✅

---

### #1
run this command.. ⬇️
```bash
if ! command -v git >/dev/null 2>&1; then


printf "Program git is not installed...\nPlease enter the password to continue...\nProceeding to install..."


if  command -v  sudo >/dev/null 2>&1; then 
sudo apt install git -y;

else 
apt install git -y;

fi;
fi;
```



Then this
```git

cd ~/
git clone "https://github.com/kanmanoor-karthik/clab.git" \
&& \
echo "Git cloned Successfully "
```

This clones the remote (online) files into your system.

---

### #2

**Run server as:**
```sh
python3 ~/clab/serverNEW.py
```
This will host server port 8000.

**Run client as:**
```sh
python3 ~/clab/client.py
```

---

## As an alternative... 🔄

You can directly download the zip from github, extract files, and navigate the terminal through your file location, where you have extracted.

##### Then run it using python3

server:
```sh
python3 serverNEW.py
```

client:
```sh
python3 client.py
```

##### Note:
Make sure these two commands run on the devices on same local network 🌐.\
You can use the same devices, but two different terminal windows.\
This has ip of 10.3.4.142, which may not be suitable for other systems, and may has to assign manually.

---

### Thats it ... You are good to go ✅

## Now,

### Connecting to the server: 🔌

We have two methods.

1. According to CLAB 301, you can just type "clab" in the host field. Thats it. Then enter the username for uniqueness ✨.

2. Manually find the ip address and port from files. Insert them directly instead of "clab". It will ask for port. Default value is 8000 🔑.

---

> If you see, connected ✅, you are good to go. Else try restarting the files 🔄.
>
> You can start chatting 💬...



# Contributors

> [Batman](http://github.com/kanmanoor-karthik)\
> [Flashman](http://github.com/kummarirahul1980)
