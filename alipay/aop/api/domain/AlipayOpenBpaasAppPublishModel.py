#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBpaasAppPublishModel(object):

    def __init__(self):
        self._app_version = None
        self._bpaas_app_id = None
        self._change_log = None
        self._file_digest = None
        self._file_md_5 = None
        self._package_file_size = None
        self._scm_download_url = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bpaas_app_id(self):
        return self._bpaas_app_id

    @bpaas_app_id.setter
    def bpaas_app_id(self, value):
        self._bpaas_app_id = value
    @property
    def change_log(self):
        return self._change_log

    @change_log.setter
    def change_log(self, value):
        self._change_log = value
    @property
    def file_digest(self):
        return self._file_digest

    @file_digest.setter
    def file_digest(self, value):
        self._file_digest = value
    @property
    def file_md_5(self):
        return self._file_md_5

    @file_md_5.setter
    def file_md_5(self, value):
        self._file_md_5 = value
    @property
    def package_file_size(self):
        return self._package_file_size

    @package_file_size.setter
    def package_file_size(self, value):
        self._package_file_size = value
    @property
    def scm_download_url(self):
        return self._scm_download_url

    @scm_download_url.setter
    def scm_download_url(self, value):
        self._scm_download_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.bpaas_app_id:
            if hasattr(self.bpaas_app_id, 'to_alipay_dict'):
                params['bpaas_app_id'] = self.bpaas_app_id.to_alipay_dict()
            else:
                params['bpaas_app_id'] = self.bpaas_app_id
        if self.change_log:
            if hasattr(self.change_log, 'to_alipay_dict'):
                params['change_log'] = self.change_log.to_alipay_dict()
            else:
                params['change_log'] = self.change_log
        if self.file_digest:
            if hasattr(self.file_digest, 'to_alipay_dict'):
                params['file_digest'] = self.file_digest.to_alipay_dict()
            else:
                params['file_digest'] = self.file_digest
        if self.file_md_5:
            if hasattr(self.file_md_5, 'to_alipay_dict'):
                params['file_md_5'] = self.file_md_5.to_alipay_dict()
            else:
                params['file_md_5'] = self.file_md_5
        if self.package_file_size:
            if hasattr(self.package_file_size, 'to_alipay_dict'):
                params['package_file_size'] = self.package_file_size.to_alipay_dict()
            else:
                params['package_file_size'] = self.package_file_size
        if self.scm_download_url:
            if hasattr(self.scm_download_url, 'to_alipay_dict'):
                params['scm_download_url'] = self.scm_download_url.to_alipay_dict()
            else:
                params['scm_download_url'] = self.scm_download_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBpaasAppPublishModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bpaas_app_id' in d:
            o.bpaas_app_id = d['bpaas_app_id']
        if 'change_log' in d:
            o.change_log = d['change_log']
        if 'file_digest' in d:
            o.file_digest = d['file_digest']
        if 'file_md_5' in d:
            o.file_md_5 = d['file_md_5']
        if 'package_file_size' in d:
            o.package_file_size = d['package_file_size']
        if 'scm_download_url' in d:
            o.scm_download_url = d['scm_download_url']
        return o


