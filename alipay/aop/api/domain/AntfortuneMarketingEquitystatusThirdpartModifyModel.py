#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinEquityInfo import FinEquityInfo
from alipay.aop.api.domain.FinUserInfo import FinUserInfo


class AntfortuneMarketingEquitystatusThirdpartModifyModel(object):

    def __init__(self):
        self._equity_code = None
        self._equity_info = None
        self._out_biz_no = None
        self._source = None
        self._status = None
        self._update_time = None
        self._user_info = None

    @property
    def equity_code(self):
        return self._equity_code

    @equity_code.setter
    def equity_code(self, value):
        self._equity_code = value
    @property
    def equity_info(self):
        return self._equity_info

    @equity_info.setter
    def equity_info(self, value):
        if isinstance(value, FinEquityInfo):
            self._equity_info = value
        else:
            self._equity_info = FinEquityInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, value):
        if isinstance(value, FinUserInfo):
            self._user_info = value
        else:
            self._user_info = FinUserInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.equity_code:
            if hasattr(self.equity_code, 'to_alipay_dict'):
                params['equity_code'] = self.equity_code.to_alipay_dict()
            else:
                params['equity_code'] = self.equity_code
        if self.equity_info:
            if hasattr(self.equity_info, 'to_alipay_dict'):
                params['equity_info'] = self.equity_info.to_alipay_dict()
            else:
                params['equity_info'] = self.equity_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.user_info:
            if hasattr(self.user_info, 'to_alipay_dict'):
                params['user_info'] = self.user_info.to_alipay_dict()
            else:
                params['user_info'] = self.user_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneMarketingEquitystatusThirdpartModifyModel()
        if 'equity_code' in d:
            o.equity_code = d['equity_code']
        if 'equity_info' in d:
            o.equity_info = d['equity_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'user_info' in d:
            o.user_info = d['user_info']
        return o


