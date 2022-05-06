#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCityserviceOpeneventAppModifyModel(object):

    def __init__(self):
        self._app_code = None
        self._biz_code = None
        self._service_desc = None
        self._service_func = None
        self._service_guide = None
        self._service_name = None
        self._service_snapshot = None
        self._service_template_config = None
        self._service_type = None
        self._service_url = None
        self._service_videos = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_func(self):
        return self._service_func

    @service_func.setter
    def service_func(self, value):
        self._service_func = value
    @property
    def service_guide(self):
        return self._service_guide

    @service_guide.setter
    def service_guide(self, value):
        self._service_guide = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_snapshot(self):
        return self._service_snapshot

    @service_snapshot.setter
    def service_snapshot(self, value):
        self._service_snapshot = value
    @property
    def service_template_config(self):
        return self._service_template_config

    @service_template_config.setter
    def service_template_config(self, value):
        self._service_template_config = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def service_videos(self):
        return self._service_videos

    @service_videos.setter
    def service_videos(self, value):
        self._service_videos = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_func:
            if hasattr(self.service_func, 'to_alipay_dict'):
                params['service_func'] = self.service_func.to_alipay_dict()
            else:
                params['service_func'] = self.service_func
        if self.service_guide:
            if hasattr(self.service_guide, 'to_alipay_dict'):
                params['service_guide'] = self.service_guide.to_alipay_dict()
            else:
                params['service_guide'] = self.service_guide
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_snapshot:
            if hasattr(self.service_snapshot, 'to_alipay_dict'):
                params['service_snapshot'] = self.service_snapshot.to_alipay_dict()
            else:
                params['service_snapshot'] = self.service_snapshot
        if self.service_template_config:
            if hasattr(self.service_template_config, 'to_alipay_dict'):
                params['service_template_config'] = self.service_template_config.to_alipay_dict()
            else:
                params['service_template_config'] = self.service_template_config
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        if self.service_videos:
            if hasattr(self.service_videos, 'to_alipay_dict'):
                params['service_videos'] = self.service_videos.to_alipay_dict()
            else:
                params['service_videos'] = self.service_videos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceOpeneventAppModifyModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_func' in d:
            o.service_func = d['service_func']
        if 'service_guide' in d:
            o.service_guide = d['service_guide']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_snapshot' in d:
            o.service_snapshot = d['service_snapshot']
        if 'service_template_config' in d:
            o.service_template_config = d['service_template_config']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'service_videos' in d:
            o.service_videos = d['service_videos']
        return o


