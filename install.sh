# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install.sh                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danbarbo <danbarbo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/06 16:10:32 by danbarbo          #+#    #+#              #
#    Updated: 2023/11/06 18:55:09 by danbarbo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

mkdir -p /tmp/norminette_br
git clone https://github.com/DanielSurf10/norminette_br.git /tmp/norminette_br
git clone -b '3.3.51' --single-branch https://github.com/42School/norminette.git /tmp/norminette_br
rm -rf /tmp/norminette_br/norminette/norm_error.py
cp /tmp/norm_error.py /tmp/norminette_br/norminette/norm_error.py
pip3 install /tmp/norminette_br --no-warn-script-location
cat ~/.zshrc | grep -q "norminette" || echo echo "alias norminette=~/.local/bin/norminette" >> ~/.zshrc
rm -rf /tmp/norminette_br
