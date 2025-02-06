#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditbenefitFuncardflagQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._funk_edu_quan = None
        self._open_id = None
        self._query_hb_sign_flag = None
        self._query_mobile = None
        self._query_youth = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def funk_edu_quan(self):
        return self._funk_edu_quan

    @funk_edu_quan.setter
    def funk_edu_quan(self, value):
        self._funk_edu_quan = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query_hb_sign_flag(self):
        return self._query_hb_sign_flag

    @query_hb_sign_flag.setter
    def query_hb_sign_flag(self, value):
        self._query_hb_sign_flag = value
    @property
    def query_mobile(self):
        return self._query_mobile

    @query_mobile.setter
    def query_mobile(self, value):
        self._query_mobile = value
    @property
    def query_youth(self):
        return self._query_youth

    @query_youth.setter
    def query_youth(self, value):
        self._query_youth = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.funk_edu_quan:
            if hasattr(self.funk_edu_quan, 'to_alipay_dict'):
                params['funk_edu_quan'] = self.funk_edu_quan.to_alipay_dict()
            else:
                params['funk_edu_quan'] = self.funk_edu_quan
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query_hb_sign_flag:
            if hasattr(self.query_hb_sign_flag, 'to_alipay_dict'):
                params['query_hb_sign_flag'] = self.query_hb_sign_flag.to_alipay_dict()
            else:
                params['query_hb_sign_flag'] = self.query_hb_sign_flag
        if self.query_mobile:
            if hasattr(self.query_mobile, 'to_alipay_dict'):
                params['query_mobile'] = self.query_mobile.to_alipay_dict()
            else:
                params['query_mobile'] = self.query_mobile
        if self.query_youth:
            if hasattr(self.query_youth, 'to_alipay_dict'):
                params['query_youth'] = self.query_youth.to_alipay_dict()
            else:
                params['query_youth'] = self.query_youth
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditbenefitFuncardflagQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'funk_edu_quan' in d:
            o.funk_edu_quan = d['funk_edu_quan']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query_hb_sign_flag' in d:
            o.query_hb_sign_flag = d['query_hb_sign_flag']
        if 'query_mobile' in d:
            o.query_mobile = d['query_mobile']
        if 'query_youth' in d:
            o.query_youth = d['query_youth']
        return o


