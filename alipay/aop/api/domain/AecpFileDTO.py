#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AliEmployeeDTO import AliEmployeeDTO


class AecpFileDTO(object):

    def __init__(self):
        self._file_size = None
        self._id = None
        self._name = None
        self._preview_url = None
        self._upload_time = None
        self._uploader = None
        self._url = None

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value
    @property
    def uploader(self):
        return self._uploader

    @uploader.setter
    def uploader(self, value):
        if isinstance(value, AliEmployeeDTO):
            self._uploader = value
        else:
            self._uploader = AliEmployeeDTO.from_alipay_dict(value)
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        if self.uploader:
            if hasattr(self.uploader, 'to_alipay_dict'):
                params['uploader'] = self.uploader.to_alipay_dict()
            else:
                params['uploader'] = self.uploader
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AecpFileDTO()
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        if 'uploader' in d:
            o.uploader = d['uploader']
        if 'url' in d:
            o.url = d['url']
        return o


