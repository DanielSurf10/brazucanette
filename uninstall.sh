# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    uninstall.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danbarbo <danbarbo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/06 17:35:48 by danbarbo          #+#    #+#              #
#    Updated: 2023/11/08 14:07:37 by danbarbo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

pip3 uninstall norminette
# cat ~/.zshrc | grep -v "norminette" > /tmp/.zshrc && mv /tmp/.zshrc ~/.zshrc
# rm -f /tmp/.zshrc
# source ~/.zshrc
