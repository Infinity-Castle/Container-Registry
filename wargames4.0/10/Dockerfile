FROM ubuntu:latest

LABEL org.opencontainers.image.source=https://github.com/Walchand-Linux-Users-Group/linux-diary

RUN apt-get update

RUN mkdir /home/wlug

WORKDIR /home/wlug

RUN apt install stegsnow

RUN echo "Well, you found me but you are still missing me !! \nLet's try another way. I heard you are very good at googling, let's start with that. Try to google me, maybe I am hidden or maybe I am not. \nWait, why are you still reading me? Go and google me to find me !!!">>visible.txt

RUN stegsnow -C -m 'FLAG is 192168188090' visible.txt .hidden.txt

WORKDIR /home

RUN echo "\n\n\n1) I guess, the actual game starts now !!! \n2) Is the file hidden ???\n3) Possible Commands for the task -> cat, cd, ls, ____snow \n\nAll The Best !!!">>README

RUN chmod 444 README

CMD ["/bin/bash"]