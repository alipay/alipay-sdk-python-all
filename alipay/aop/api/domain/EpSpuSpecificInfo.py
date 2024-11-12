#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpSpuSpecificInfo(object):

    def __init__(self):
        self._cate_1_code_cbu = None
        self._cate_1_code_std = None
        self._cate_1_name_cbu = None
        self._cate_1_name_std = None
        self._cate_1_pro_cnt = None
        self._cate_2_code_cbu = None
        self._cate_2_code_std = None
        self._cate_2_name_cbu = None
        self._cate_2_name_std = None
        self._cate_2_pro_cnt = None
        self._cate_3_code_cbu = None
        self._cate_3_name_cbu = None
        self._cate_3_pro_cnt = None
        self._confidence = None
        self._confindence = None
        self._item_id = None
        self._item_mark_date = None
        self._item_name = None

    @property
    def cate_1_code_cbu(self):
        return self._cate_1_code_cbu

    @cate_1_code_cbu.setter
    def cate_1_code_cbu(self, value):
        self._cate_1_code_cbu = value
    @property
    def cate_1_code_std(self):
        return self._cate_1_code_std

    @cate_1_code_std.setter
    def cate_1_code_std(self, value):
        self._cate_1_code_std = value
    @property
    def cate_1_name_cbu(self):
        return self._cate_1_name_cbu

    @cate_1_name_cbu.setter
    def cate_1_name_cbu(self, value):
        self._cate_1_name_cbu = value
    @property
    def cate_1_name_std(self):
        return self._cate_1_name_std

    @cate_1_name_std.setter
    def cate_1_name_std(self, value):
        self._cate_1_name_std = value
    @property
    def cate_1_pro_cnt(self):
        return self._cate_1_pro_cnt

    @cate_1_pro_cnt.setter
    def cate_1_pro_cnt(self, value):
        self._cate_1_pro_cnt = value
    @property
    def cate_2_code_cbu(self):
        return self._cate_2_code_cbu

    @cate_2_code_cbu.setter
    def cate_2_code_cbu(self, value):
        self._cate_2_code_cbu = value
    @property
    def cate_2_code_std(self):
        return self._cate_2_code_std

    @cate_2_code_std.setter
    def cate_2_code_std(self, value):
        self._cate_2_code_std = value
    @property
    def cate_2_name_cbu(self):
        return self._cate_2_name_cbu

    @cate_2_name_cbu.setter
    def cate_2_name_cbu(self, value):
        self._cate_2_name_cbu = value
    @property
    def cate_2_name_std(self):
        return self._cate_2_name_std

    @cate_2_name_std.setter
    def cate_2_name_std(self, value):
        self._cate_2_name_std = value
    @property
    def cate_2_pro_cnt(self):
        return self._cate_2_pro_cnt

    @cate_2_pro_cnt.setter
    def cate_2_pro_cnt(self, value):
        self._cate_2_pro_cnt = value
    @property
    def cate_3_code_cbu(self):
        return self._cate_3_code_cbu

    @cate_3_code_cbu.setter
    def cate_3_code_cbu(self, value):
        self._cate_3_code_cbu = value
    @property
    def cate_3_name_cbu(self):
        return self._cate_3_name_cbu

    @cate_3_name_cbu.setter
    def cate_3_name_cbu(self, value):
        self._cate_3_name_cbu = value
    @property
    def cate_3_pro_cnt(self):
        return self._cate_3_pro_cnt

    @cate_3_pro_cnt.setter
    def cate_3_pro_cnt(self, value):
        self._cate_3_pro_cnt = value
    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value
    @property
    def confindence(self):
        return self._confindence

    @confindence.setter
    def confindence(self, value):
        self._confindence = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_mark_date(self):
        return self._item_mark_date

    @item_mark_date.setter
    def item_mark_date(self, value):
        self._item_mark_date = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_1_code_cbu:
            if hasattr(self.cate_1_code_cbu, 'to_alipay_dict'):
                params['cate_1_code_cbu'] = self.cate_1_code_cbu.to_alipay_dict()
            else:
                params['cate_1_code_cbu'] = self.cate_1_code_cbu
        if self.cate_1_code_std:
            if hasattr(self.cate_1_code_std, 'to_alipay_dict'):
                params['cate_1_code_std'] = self.cate_1_code_std.to_alipay_dict()
            else:
                params['cate_1_code_std'] = self.cate_1_code_std
        if self.cate_1_name_cbu:
            if hasattr(self.cate_1_name_cbu, 'to_alipay_dict'):
                params['cate_1_name_cbu'] = self.cate_1_name_cbu.to_alipay_dict()
            else:
                params['cate_1_name_cbu'] = self.cate_1_name_cbu
        if self.cate_1_name_std:
            if hasattr(self.cate_1_name_std, 'to_alipay_dict'):
                params['cate_1_name_std'] = self.cate_1_name_std.to_alipay_dict()
            else:
                params['cate_1_name_std'] = self.cate_1_name_std
        if self.cate_1_pro_cnt:
            if hasattr(self.cate_1_pro_cnt, 'to_alipay_dict'):
                params['cate_1_pro_cnt'] = self.cate_1_pro_cnt.to_alipay_dict()
            else:
                params['cate_1_pro_cnt'] = self.cate_1_pro_cnt
        if self.cate_2_code_cbu:
            if hasattr(self.cate_2_code_cbu, 'to_alipay_dict'):
                params['cate_2_code_cbu'] = self.cate_2_code_cbu.to_alipay_dict()
            else:
                params['cate_2_code_cbu'] = self.cate_2_code_cbu
        if self.cate_2_code_std:
            if hasattr(self.cate_2_code_std, 'to_alipay_dict'):
                params['cate_2_code_std'] = self.cate_2_code_std.to_alipay_dict()
            else:
                params['cate_2_code_std'] = self.cate_2_code_std
        if self.cate_2_name_cbu:
            if hasattr(self.cate_2_name_cbu, 'to_alipay_dict'):
                params['cate_2_name_cbu'] = self.cate_2_name_cbu.to_alipay_dict()
            else:
                params['cate_2_name_cbu'] = self.cate_2_name_cbu
        if self.cate_2_name_std:
            if hasattr(self.cate_2_name_std, 'to_alipay_dict'):
                params['cate_2_name_std'] = self.cate_2_name_std.to_alipay_dict()
            else:
                params['cate_2_name_std'] = self.cate_2_name_std
        if self.cate_2_pro_cnt:
            if hasattr(self.cate_2_pro_cnt, 'to_alipay_dict'):
                params['cate_2_pro_cnt'] = self.cate_2_pro_cnt.to_alipay_dict()
            else:
                params['cate_2_pro_cnt'] = self.cate_2_pro_cnt
        if self.cate_3_code_cbu:
            if hasattr(self.cate_3_code_cbu, 'to_alipay_dict'):
                params['cate_3_code_cbu'] = self.cate_3_code_cbu.to_alipay_dict()
            else:
                params['cate_3_code_cbu'] = self.cate_3_code_cbu
        if self.cate_3_name_cbu:
            if hasattr(self.cate_3_name_cbu, 'to_alipay_dict'):
                params['cate_3_name_cbu'] = self.cate_3_name_cbu.to_alipay_dict()
            else:
                params['cate_3_name_cbu'] = self.cate_3_name_cbu
        if self.cate_3_pro_cnt:
            if hasattr(self.cate_3_pro_cnt, 'to_alipay_dict'):
                params['cate_3_pro_cnt'] = self.cate_3_pro_cnt.to_alipay_dict()
            else:
                params['cate_3_pro_cnt'] = self.cate_3_pro_cnt
        if self.confidence:
            if hasattr(self.confidence, 'to_alipay_dict'):
                params['confidence'] = self.confidence.to_alipay_dict()
            else:
                params['confidence'] = self.confidence
        if self.confindence:
            if hasattr(self.confindence, 'to_alipay_dict'):
                params['confindence'] = self.confindence.to_alipay_dict()
            else:
                params['confindence'] = self.confindence
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_mark_date:
            if hasattr(self.item_mark_date, 'to_alipay_dict'):
                params['item_mark_date'] = self.item_mark_date.to_alipay_dict()
            else:
                params['item_mark_date'] = self.item_mark_date
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpSpuSpecificInfo()
        if 'cate_1_code_cbu' in d:
            o.cate_1_code_cbu = d['cate_1_code_cbu']
        if 'cate_1_code_std' in d:
            o.cate_1_code_std = d['cate_1_code_std']
        if 'cate_1_name_cbu' in d:
            o.cate_1_name_cbu = d['cate_1_name_cbu']
        if 'cate_1_name_std' in d:
            o.cate_1_name_std = d['cate_1_name_std']
        if 'cate_1_pro_cnt' in d:
            o.cate_1_pro_cnt = d['cate_1_pro_cnt']
        if 'cate_2_code_cbu' in d:
            o.cate_2_code_cbu = d['cate_2_code_cbu']
        if 'cate_2_code_std' in d:
            o.cate_2_code_std = d['cate_2_code_std']
        if 'cate_2_name_cbu' in d:
            o.cate_2_name_cbu = d['cate_2_name_cbu']
        if 'cate_2_name_std' in d:
            o.cate_2_name_std = d['cate_2_name_std']
        if 'cate_2_pro_cnt' in d:
            o.cate_2_pro_cnt = d['cate_2_pro_cnt']
        if 'cate_3_code_cbu' in d:
            o.cate_3_code_cbu = d['cate_3_code_cbu']
        if 'cate_3_name_cbu' in d:
            o.cate_3_name_cbu = d['cate_3_name_cbu']
        if 'cate_3_pro_cnt' in d:
            o.cate_3_pro_cnt = d['cate_3_pro_cnt']
        if 'confidence' in d:
            o.confidence = d['confidence']
        if 'confindence' in d:
            o.confindence = d['confindence']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_mark_date' in d:
            o.item_mark_date = d['item_mark_date']
        if 'item_name' in d:
            o.item_name = d['item_name']
        return o


