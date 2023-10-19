##
## EPITECH PROJECT, 2020
## gomoku
## File description:
## Makefile
##

NAME	=	./pbrain-gomoku-ai

SRC		=	./main.py

CP		=	cp $(SRC) $(NAME)

##peut etre sans 
CHMOD	=	chmod 777 $(NAME)

RM		=	rm -rf

all:	$(NAME)

$(NAME):
	$(CP)
	$(CHMOD)

clean:
	$(RM) $(NAME)

fclean:
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re