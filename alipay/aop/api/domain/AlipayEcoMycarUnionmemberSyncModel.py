#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarUnionmemberSyncModel(object):

    def __init__(self):
        self._biz_card_no = None
        self._brand_id = None
        self._card_template_id = None
        self._level = None
        self._manufacturer_id = None
        self._model_id = None
        self._occur_time = None
        self._open_date = None
        self._open_id = None
        self._opt = None
        self._series_id = None
        self._user_id = None
        self._valid_date = None

    @property
    def biz_card_no(self):
        return self._biz_card_no

    @biz_card_no.setter
    def biz_card_no(self, value):
        self._biz_card_no = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def manufacturer_id(self):
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, value):
        self._manufacturer_id = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, value):
        self._open_date = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def opt(self):
        return self._opt

    @opt.setter
    def opt(self, value):
        self._opt = value
    @property
    def series_id(self):
        return self._series_id

    @series_id.setter
    def series_id(self, value):
        self._series_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_card_no:
            if hasattr(self.biz_card_no, 'to_alipay_dict'):
                params['biz_card_no'] = self.biz_card_no.to_alipay_dict()
            else:
                params['biz_card_no'] = self.biz_card_no
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.manufacturer_id:
            if hasattr(self.manufacturer_id, 'to_alipay_dict'):
                params['manufacturer_id'] = self.manufacturer_id.to_alipay_dict()
            else:
                params['manufacturer_id'] = self.manufacturer_id
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.open_date:
            if hasattr(self.open_date, 'to_alipay_dict'):
                params['open_date'] = self.open_date.to_alipay_dict()
            else:
                params['open_date'] = self.open_date
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.opt:
            if hasattr(self.opt, 'to_alipay_dict'):
                params['opt'] = self.opt.to_alipay_dict()
            else:
                params['opt'] = self.opt
        if self.series_id:
            if hasattr(self.series_id, 'to_alipay_dict'):
                params['series_id'] = self.series_id.to_alipay_dict()
            else:
                params['series_id'] = self.series_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_date:
            if hasattr(self.valid_date, 'to_alipay_dict'):
                params['valid_date'] = self.valid_date.to_alipay_dict()
            else:
                params['valid_date'] = self.valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarUnionmemberSyncModel()
        if 'biz_card_no' in d:
            o.biz_card_no = d['biz_card_no']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'level' in d:
            o.level = d['level']
        if 'manufacturer_id' in d:
            o.manufacturer_id = d['manufacturer_id']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'open_date' in d:
            o.open_date = d['open_date']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'opt' in d:
            o.opt = d['opt']
        if 'series_id' in d:
            o.series_id = d['series_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_date' in d:
            o.valid_date = d['valid_date']
        return o


