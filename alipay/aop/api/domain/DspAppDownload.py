#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DspAppDownloadExtInfo import DspAppDownloadExtInfo


class DspAppDownload(object):

    def __init__(self):
        self._app_download_ext_info = None
        self._app_version = None
        self._download_url = None
        self._package_name = None
        self._platform = None

    @property
    def app_download_ext_info(self):
        return self._app_download_ext_info

    @app_download_ext_info.setter
    def app_download_ext_info(self, value):
        if isinstance(value, list):
            self._app_download_ext_info = list()
            for i in value:
                if isinstance(i, DspAppDownloadExtInfo):
                    self._app_download_ext_info.append(i)
                else:
                    self._app_download_ext_info.append(DspAppDownloadExtInfo.from_alipay_dict(i))
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_download_ext_info:
            if isinstance(self.app_download_ext_info, list):
                for i in range(0, len(self.app_download_ext_info)):
                    element = self.app_download_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_download_ext_info[i] = element.to_alipay_dict()
            if hasattr(self.app_download_ext_info, 'to_alipay_dict'):
                params['app_download_ext_info'] = self.app_download_ext_info.to_alipay_dict()
            else:
                params['app_download_ext_info'] = self.app_download_ext_info
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DspAppDownload()
        if 'app_download_ext_info' in d:
            o.app_download_ext_info = d['app_download_ext_info']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'platform' in d:
            o.platform = d['platform']
        return o


