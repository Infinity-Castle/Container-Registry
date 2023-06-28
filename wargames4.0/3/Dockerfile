FROM ubuntu:latest

LABEL org.opencontainers.image.source=https://github.com/Walchand-Linux-Users-Group/linux-diary

RUN apt-get update

RUN mkdir /home/wlug

WORKDIR /home/wlug

RUN echo "Come on, are you really looking into the files ???">.history

RUN chmod 444 .history

WORKDIR /home

RUN echo "echo 'Your Flag = WLUG{5666852796}'">>.bash_history

RUN chmod 444 .bash_history

RUN echo "\n\n\n1) Do container have History ??? \n\n\nPossible Commands for the task -> cat, history \n\n\nAll The Best !!!">README

RUN chmod 444 README

WORKDIR /home/wlug

CMD ["/bin/bash"]