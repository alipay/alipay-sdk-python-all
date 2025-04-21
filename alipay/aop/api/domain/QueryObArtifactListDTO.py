#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryObArtifactListDTO(object):

    def __init__(self):
        self._artifact_version = None
        self._download_url = None
        self._fullname = None
        self._project_name = None
        self._size = None
        self._unique_data_key = None
        self._use_type_str = None
        self._version_tag_str = None

    @property
    def artifact_version(self):
        return self._artifact_version

    @artifact_version.setter
    def artifact_version(self, value):
        self._artifact_version = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, value):
        self._fullname = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def unique_data_key(self):
        return self._unique_data_key

    @unique_data_key.setter
    def unique_data_key(self, value):
        self._unique_data_key = value
    @property
    def use_type_str(self):
        return self._use_type_str

    @use_type_str.setter
    def use_type_str(self, value):
        self._use_type_str = value
    @property
    def version_tag_str(self):
        return self._version_tag_str

    @version_tag_str.setter
    def version_tag_str(self, value):
        self._version_tag_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.artifact_version:
            if hasattr(self.artifact_version, 'to_alipay_dict'):
                params['artifact_version'] = self.artifact_version.to_alipay_dict()
            else:
                params['artifact_version'] = self.artifact_version
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.fullname:
            if hasattr(self.fullname, 'to_alipay_dict'):
                params['fullname'] = self.fullname.to_alipay_dict()
            else:
                params['fullname'] = self.fullname
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.unique_data_key:
            if hasattr(self.unique_data_key, 'to_alipay_dict'):
                params['unique_data_key'] = self.unique_data_key.to_alipay_dict()
            else:
                params['unique_data_key'] = self.unique_data_key
        if self.use_type_str:
            if hasattr(self.use_type_str, 'to_alipay_dict'):
                params['use_type_str'] = self.use_type_str.to_alipay_dict()
            else:
                params['use_type_str'] = self.use_type_str
        if self.version_tag_str:
            if hasattr(self.version_tag_str, 'to_alipay_dict'):
                params['version_tag_str'] = self.version_tag_str.to_alipay_dict()
            else:
                params['version_tag_str'] = self.version_tag_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryObArtifactListDTO()
        if 'artifact_version' in d:
            o.artifact_version = d['artifact_version']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'fullname' in d:
            o.fullname = d['fullname']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'size' in d:
            o.size = d['size']
        if 'unique_data_key' in d:
            o.unique_data_key = d['unique_data_key']
        if 'use_type_str' in d:
            o.use_type_str = d['use_type_str']
        if 'version_tag_str' in d:
            o.version_tag_str = d['version_tag_str']
        return o


