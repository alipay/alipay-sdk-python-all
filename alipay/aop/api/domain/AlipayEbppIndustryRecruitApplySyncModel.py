#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRecruitApplySyncModel(object):

    def __init__(self):
        self._apply_change_time = None
        self._apply_open_id = None
        self._apply_status = None
        self._apply_time = None
        self._apply_user_id = None
        self._biz_id = None
        self._client_apply_url = None
        self._inappropriate_reason = None
        self._inter_address = None
        self._inter_time = None
        self._iot_sn = None
        self._out_apply_id = None
        self._out_job_id = None
        self._out_user_id = None
        self._server_apply_url = None
        self._source = None

    @property
    def apply_change_time(self):
        return self._apply_change_time

    @apply_change_time.setter
    def apply_change_time(self, value):
        self._apply_change_time = value
    @property
    def apply_open_id(self):
        return self._apply_open_id

    @apply_open_id.setter
    def apply_open_id(self, value):
        self._apply_open_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def apply_user_id(self):
        return self._apply_user_id

    @apply_user_id.setter
    def apply_user_id(self, value):
        self._apply_user_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def client_apply_url(self):
        return self._client_apply_url

    @client_apply_url.setter
    def client_apply_url(self, value):
        self._client_apply_url = value
    @property
    def inappropriate_reason(self):
        return self._inappropriate_reason

    @inappropriate_reason.setter
    def inappropriate_reason(self, value):
        self._inappropriate_reason = value
    @property
    def inter_address(self):
        return self._inter_address

    @inter_address.setter
    def inter_address(self, value):
        self._inter_address = value
    @property
    def inter_time(self):
        return self._inter_time

    @inter_time.setter
    def inter_time(self, value):
        self._inter_time = value
    @property
    def iot_sn(self):
        return self._iot_sn

    @iot_sn.setter
    def iot_sn(self, value):
        self._iot_sn = value
    @property
    def out_apply_id(self):
        return self._out_apply_id

    @out_apply_id.setter
    def out_apply_id(self, value):
        self._out_apply_id = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def server_apply_url(self):
        return self._server_apply_url

    @server_apply_url.setter
    def server_apply_url(self, value):
        self._server_apply_url = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_change_time:
            if hasattr(self.apply_change_time, 'to_alipay_dict'):
                params['apply_change_time'] = self.apply_change_time.to_alipay_dict()
            else:
                params['apply_change_time'] = self.apply_change_time
        if self.apply_open_id:
            if hasattr(self.apply_open_id, 'to_alipay_dict'):
                params['apply_open_id'] = self.apply_open_id.to_alipay_dict()
            else:
                params['apply_open_id'] = self.apply_open_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.apply_user_id:
            if hasattr(self.apply_user_id, 'to_alipay_dict'):
                params['apply_user_id'] = self.apply_user_id.to_alipay_dict()
            else:
                params['apply_user_id'] = self.apply_user_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.client_apply_url:
            if hasattr(self.client_apply_url, 'to_alipay_dict'):
                params['client_apply_url'] = self.client_apply_url.to_alipay_dict()
            else:
                params['client_apply_url'] = self.client_apply_url
        if self.inappropriate_reason:
            if hasattr(self.inappropriate_reason, 'to_alipay_dict'):
                params['inappropriate_reason'] = self.inappropriate_reason.to_alipay_dict()
            else:
                params['inappropriate_reason'] = self.inappropriate_reason
        if self.inter_address:
            if hasattr(self.inter_address, 'to_alipay_dict'):
                params['inter_address'] = self.inter_address.to_alipay_dict()
            else:
                params['inter_address'] = self.inter_address
        if self.inter_time:
            if hasattr(self.inter_time, 'to_alipay_dict'):
                params['inter_time'] = self.inter_time.to_alipay_dict()
            else:
                params['inter_time'] = self.inter_time
        if self.iot_sn:
            if hasattr(self.iot_sn, 'to_alipay_dict'):
                params['iot_sn'] = self.iot_sn.to_alipay_dict()
            else:
                params['iot_sn'] = self.iot_sn
        if self.out_apply_id:
            if hasattr(self.out_apply_id, 'to_alipay_dict'):
                params['out_apply_id'] = self.out_apply_id.to_alipay_dict()
            else:
                params['out_apply_id'] = self.out_apply_id
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.server_apply_url:
            if hasattr(self.server_apply_url, 'to_alipay_dict'):
                params['server_apply_url'] = self.server_apply_url.to_alipay_dict()
            else:
                params['server_apply_url'] = self.server_apply_url
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRecruitApplySyncModel()
        if 'apply_change_time' in d:
            o.apply_change_time = d['apply_change_time']
        if 'apply_open_id' in d:
            o.apply_open_id = d['apply_open_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'apply_user_id' in d:
            o.apply_user_id = d['apply_user_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'client_apply_url' in d:
            o.client_apply_url = d['client_apply_url']
        if 'inappropriate_reason' in d:
            o.inappropriate_reason = d['inappropriate_reason']
        if 'inter_address' in d:
            o.inter_address = d['inter_address']
        if 'inter_time' in d:
            o.inter_time = d['inter_time']
        if 'iot_sn' in d:
            o.iot_sn = d['iot_sn']
        if 'out_apply_id' in d:
            o.out_apply_id = d['out_apply_id']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'server_apply_url' in d:
            o.server_apply_url = d['server_apply_url']
        if 'source' in d:
            o.source = d['source']
        return o


