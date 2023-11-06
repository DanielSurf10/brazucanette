# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install.sh                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danbarbo <danbarbo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/06 16:10:32 by danbarbo          #+#    #+#              #
#    Updated: 2023/11/06 19:11:25 by danbarbo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

mkdir -p /tmp/norminette_br
git clone -b '3.3.51' --single-branch https://github.com/42School/norminette.git /tmp/norminette_br
rm -rf /tmp/norminette_br/norminette/norm_error.py
curl -o /tmp/norminette_br/norminette/norm_error.py https://raw.githubusercontent.com/DanielSurf10/brazucanette/main/norm_error.py
pip3 install /tmp/norminette_br --no-warn-script-location
cat ~/.zshrc | grep -q "norminette" || echo echo "alias norminette=~/.local/bin/norminette" >> ~/.zshrc
rm -rf /tmp/norminette_br
