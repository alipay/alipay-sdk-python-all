#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodPlanQueryModel(object):

    def __init__(self):
        self._channel = None
        self._customer_channel = None
        self._ext_param = None
        self._org_code = None
        self._product_code = None
        self._scene = None
        self._seq_no = None
        self._site = None
        self._site_user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def customer_channel(self):
        return self._customer_channel

    @customer_channel.setter
    def customer_channel(self, value):
        self._customer_channel = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def seq_no(self):
        return self._seq_no

    @seq_no.setter
    def seq_no(self, value):
        self._seq_no = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.customer_channel:
            if hasattr(self.customer_channel, 'to_alipay_dict'):
                params['customer_channel'] = self.customer_channel.to_alipay_dict()
            else:
                params['customer_channel'] = self.customer_channel
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.seq_no:
            if hasattr(self.seq_no, 'to_alipay_dict'):
                params['seq_no'] = self.seq_no.to_alipay_dict()
            else:
                params['seq_no'] = self.seq_no
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodPlanQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'customer_channel' in d:
            o.customer_channel = d['customer_channel']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene' in d:
            o.scene = d['scene']
        if 'seq_no' in d:
            o.seq_no = d['seq_no']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        return o


