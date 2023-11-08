# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install.sh                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danbarbo <danbarbo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/06 16:10:32 by danbarbo          #+#    #+#              #
#    Updated: 2023/11/08 14:01:12 by danbarbo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

rm -rf /tmp/norminette_br
mkdir -p /tmp/norminette_br
mkdir -p ~/.local/share/norminette
git clone https://github.com/DanielSurf10/brazucanette.git /tmp/norminette_br
git clone -b '3.3.51' --single-branch https://github.com/42School/norminette.git /tmp/norminette_br/norminette
rm -rf /tmp/norminette_br/norminette/norminette/norm_error.py
cp /tmp/norminette_br/norm_error.py /tmp/norminette_br/norminette/norminette/norm_error.py
cp /tmp/norminette_br/norm_error.json ~/.local/share/norminette/norm_error.json
pip3 install /tmp/norminette_br/norminette --no-warn-script-location
# cat ~/.zshrc | grep -q "norminette" || echo "alias norminette=~/.local/bin/norminette" >> ~/.zshrc
# cat ~/.zshrc | grep -q "norminettee" || echo "alias norminete=/usr/bin/norminette" >> ~/.zshrc
rm -rf /tmp/norminette_br
