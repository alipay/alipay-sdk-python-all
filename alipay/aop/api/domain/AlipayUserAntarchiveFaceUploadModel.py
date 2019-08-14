#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArchiveFaceExtInfo import ArchiveFaceExtInfo


class AlipayUserAntarchiveFaceUploadModel(object):

    def __init__(self):
        self._biz_scene = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._ext_info = None
        self._other_portrait_url = None
        self._portrait_url = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ArchiveFaceExtInfo):
            self._ext_info = value
        else:
            self._ext_info = ArchiveFaceExtInfo.from_alipay_dict(value)
    @property
    def other_portrait_url(self):
        return self._other_portrait_url

    @other_portrait_url.setter
    def other_portrait_url(self, value):
        self._other_portrait_url = value
    @property
    def portrait_url(self):
        return self._portrait_url

    @portrait_url.setter
    def portrait_url(self, value):
        self._portrait_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.other_portrait_url:
            if hasattr(self.other_portrait_url, 'to_alipay_dict'):
                params['other_portrait_url'] = self.other_portrait_url.to_alipay_dict()
            else:
                params['other_portrait_url'] = self.other_portrait_url
        if self.portrait_url:
            if hasattr(self.portrait_url, 'to_alipay_dict'):
                params['portrait_url'] = self.portrait_url.to_alipay_dict()
            else:
                params['portrait_url'] = self.portrait_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntarchiveFaceUploadModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'other_portrait_url' in d:
            o.other_portrait_url = d['other_portrait_url']
        if 'portrait_url' in d:
            o.portrait_url = d['portrait_url']
        return o


