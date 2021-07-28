#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntforestPlantApplyModel(object):

    def __init__(self):
        self._account_id = None
        self._apply_type = None
        self._ext_info = None
        self._out_biz_no = None
        self._participant = None
        self._project_id = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def participant(self):
        return self._participant

    @participant.setter
    def participant(self, value):
        self._participant = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.participant:
            if hasattr(self.participant, 'to_alipay_dict'):
                params['participant'] = self.participant.to_alipay_dict()
            else:
                params['participant'] = self.participant
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntforestPlantApplyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'participant' in d:
            o.participant = d['participant']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


