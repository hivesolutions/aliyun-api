#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Alibaba Cloud API
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Alibaba Cloud API.
#
# Hive Alibaba Cloud API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Alibaba Cloud API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Alibaba Cloud API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

import aliyun


def get_api():
    return aliyun.API(
        base_url=appier.conf("ALIYUN_BASE_URL", aliyun.BASE_URL),
        access_key=appier.conf("ALIYUN_ACCESS_KEY"),
        secret=appier.conf("ALIYUN_SECRET"),
    )
