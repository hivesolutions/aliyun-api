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


class ObjectAPI(object):

    def create_object(self, bucket, name, data, md5=None):
        url = self.bucket_url % bucket + "%s" % appier.legacy.quote(name)
        contents = self.put(
            url,
            data=data,
            sign=True,
            resource="/%s/%s" % (bucket, name),
            md5=md5 or self._content_md5(data),
        )
        return contents

    def build_url_object(self, bucket, name):
        return self.bucket_url % bucket + "%s" % name

    def create_file_object(self, bucket, name, path, md5=None):
        return self.create_object(
            bucket,
            name,
            data=appier.file_g(path),
            md5=md5 or self._content_md5(appier.file_g(path)),
        )
