# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''
from alipay.aop.api.util.CommonUtils import get_mime_type


class FileItem(object):

    def __init__(self, file_name=None, file_content=None, mime_type=None):
        self._file_name = file_name
        self._file_content = file_content
        self._mime_type = mime_type

    def get_file_name(self):
        return self._file_name

    def get_file_content(self):
        return self._file_content

    def get_mime_type(self):
        if not self._mime_type:
            self._mime_type = get_mime_type(self.get_file_content())
        return self._mime_type


