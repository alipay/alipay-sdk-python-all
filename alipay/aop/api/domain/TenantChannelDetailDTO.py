#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TenantChannelDetailDTO(object):

    def __init__(self):
        self._channel_code = None
        self._channel_desc = None
        self._channel_id = None
        self._channel_name = None
        self._channel_status = None
        self._channel_type = None
        self._form_template_id = None
        self._pic_url = None
        self._remark = None
        self._status = None
        self._tenant_code = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_desc(self):
        return self._channel_desc

    @channel_desc.setter
    def channel_desc(self, value):
        self._channel_desc = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def channel_status(self):
        return self._channel_status

    @channel_status.setter
    def channel_status(self, value):
        self._channel_status = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def form_template_id(self):
        return self._form_template_id

    @form_template_id.setter
    def form_template_id(self, value):
        self._form_template_id = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.channel_desc:
            if hasattr(self.channel_desc, 'to_alipay_dict'):
                params['channel_desc'] = self.channel_desc.to_alipay_dict()
            else:
                params['channel_desc'] = self.channel_desc
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        if self.channel_status:
            if hasattr(self.channel_status, 'to_alipay_dict'):
                params['channel_status'] = self.channel_status.to_alipay_dict()
            else:
                params['channel_status'] = self.channel_status
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.form_template_id:
            if hasattr(self.form_template_id, 'to_alipay_dict'):
                params['form_template_id'] = self.form_template_id.to_alipay_dict()
            else:
                params['form_template_id'] = self.form_template_id
        if self.pic_url:
            if hasattr(self.pic_url, 'to_alipay_dict'):
                params['pic_url'] = self.pic_url.to_alipay_dict()
            else:
                params['pic_url'] = self.pic_url
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TenantChannelDetailDTO()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'channel_desc' in d:
            o.channel_desc = d['channel_desc']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        if 'channel_status' in d:
            o.channel_status = d['channel_status']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'form_template_id' in d:
            o.form_template_id = d['form_template_id']
        if 'pic_url' in d:
            o.pic_url = d['pic_url']
        if 'remark' in d:
            o.remark = d['remark']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


