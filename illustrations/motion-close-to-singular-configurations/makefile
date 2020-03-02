GIFS_SOURCE_DIRECTORY=/home/pedro/Desktop/catkin_ws_geometric_control/src/pendulum_description/worlds/shots/
SHOTS_SOURCE_DIRECTORY=$(GIFS_SOURCE_DIRECTORY)camera_front/
HARCODED_FILES_NAMES=default_camera_front_camera_link_my_camera_front(1)-

# I cannot include default_camera_front_camera_link_my_camera_front(1)-0001.jpg with JEMDOC
# so I need to rename this to something else

GIFS2COPY=$(wildcard $(GIFS_SOURCE_DIRECTORY)*.gif)
#remove source directory
GIFS=$(GIFS2COPY:$(GIFS_SOURCE_DIRECTORY)%=%)

SHOTS2COPY=$(wildcard $(SHOTS_SOURCE_DIRECTORY)*[0][0][0][1234].jpg)
#remove source directory
SHOTS=$(SHOTS2COPY:$(SHOTS_SOURCE_DIRECTORY)%=%)
SHOTS_RENAMED=$(SHOTS:$(HARCODED_FILES_NAMES)%=shot_%)

%.gif: $(GIFS_SOURCE_DIRECTORY)%.gif
	cp $^ $@
# echo $^
# echo $@

get_gifs: $(GIFS)
	@echo $(GIFS)
#@echo $(GIFS2COPY)

# primes (' ') everywhere because of presence of parenthesis
%.jpg: $(SHOTS_SOURCE_DIRECTORY)%.jpg
	cp '$^' '$@'
	cp '$^' $(subst $(HARCODED_FILES_NAMES),shot_, '$@')

get_shots: $(SHOTS)
	@echo '$(SHOTS_RENAMED)'
# @echo '$(SHOTS_RENAMED)'
#	@echo '$(SHOTS)'
# @echo '$(SHOTS2COPY)'
# this does not work
# @echo $(SHOTS2COPY)
# because files have parenthesis in their name
# which screws up with the shell

all: get_gifs get_shots

clean:
	rm *.gif
	rm *.jpg

# not file related targets
.PHONY: all clean get_gifs get_shots
