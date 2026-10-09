#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CareerOpenBaseInvitationDetailResult(object):

    def __init__(self):
        self._desc_msg = None
        self._detail_status = None
        self._encrypted_mobile = None
        self._out_biz_no = None
        self._out_job_id = None

    @property
    def desc_msg(self):
        return self._desc_msg

    @desc_msg.setter
    def desc_msg(self, value):
        self._desc_msg = value
    @property
    def detail_status(self):
        return self._detail_status

    @detail_status.setter
    def detail_status(self, value):
        self._detail_status = value
    @property
    def encrypted_mobile(self):
        return self._encrypted_mobile

    @encrypted_mobile.setter
    def encrypted_mobile(self, value):
        self._encrypted_mobile = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_job_id(self):
        return self._out_job_id

    @out_job_id.setter
    def out_job_id(self, value):
        self._out_job_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc_msg:
            if hasattr(self.desc_msg, 'to_alipay_dict'):
                params['desc_msg'] = self.desc_msg.to_alipay_dict()
            else:
                params['desc_msg'] = self.desc_msg
        if self.detail_status:
            if hasattr(self.detail_status, 'to_alipay_dict'):
                params['detail_status'] = self.detail_status.to_alipay_dict()
            else:
                params['detail_status'] = self.detail_status
        if self.encrypted_mobile:
            if hasattr(self.encrypted_mobile, 'to_alipay_dict'):
                params['encrypted_mobile'] = self.encrypted_mobile.to_alipay_dict()
            else:
                params['encrypted_mobile'] = self.encrypted_mobile
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_job_id:
            if hasattr(self.out_job_id, 'to_alipay_dict'):
                params['out_job_id'] = self.out_job_id.to_alipay_dict()
            else:
                params['out_job_id'] = self.out_job_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CareerOpenBaseInvitationDetailResult()
        if 'desc_msg' in d:
            o.desc_msg = d['desc_msg']
        if 'detail_status' in d:
            o.detail_status = d['detail_status']
        if 'encrypted_mobile' in d:
            o.encrypted_mobile = d['encrypted_mobile']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_job_id' in d:
            o.out_job_id = d['out_job_id']
        return o


