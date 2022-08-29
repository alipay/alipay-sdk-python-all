#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiMerchantBenefitSyncModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._ext_info = None
        self._gmt_operate = None
        self._hb_instance_id = None
        self._out_biz_no = None
        self._status = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_operate(self):
        return self._gmt_operate

    @gmt_operate.setter
    def gmt_operate(self, value):
        self._gmt_operate = value
    @property
    def hb_instance_id(self):
        return self._hb_instance_id

    @hb_instance_id.setter
    def hb_instance_id(self, value):
        self._hb_instance_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_operate:
            if hasattr(self.gmt_operate, 'to_alipay_dict'):
                params['gmt_operate'] = self.gmt_operate.to_alipay_dict()
            else:
                params['gmt_operate'] = self.gmt_operate
        if self.hb_instance_id:
            if hasattr(self.hb_instance_id, 'to_alipay_dict'):
                params['hb_instance_id'] = self.hb_instance_id.to_alipay_dict()
            else:
                params['hb_instance_id'] = self.hb_instance_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMerchantBenefitSyncModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_operate' in d:
            o.gmt_operate = d['gmt_operate']
        if 'hb_instance_id' in d:
            o.hb_instance_id = d['hb_instance_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'status' in d:
            o.status = d['status']
        return o


