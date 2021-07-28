#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduTrainExtInfo import EduTrainExtInfo
from alipay.aop.api.domain.EduTrainExtInfo import EduTrainExtInfo


class AlipayCommerceEducateTrainRecommendQueryModel(object):

    def __init__(self):
        self._biz_ext_info = None
        self._first_cate = None
        self._page_index = None
        self._page_size = None
        self._product_code = None
        self._rec_ext_info = None
        self._scene_id = None
        self._secend_cate = None
        self._sub_product_code = None
        self._user_id = None

    @property
    def biz_ext_info(self):
        return self._biz_ext_info

    @biz_ext_info.setter
    def biz_ext_info(self, value):
        if isinstance(value, EduTrainExtInfo):
            self._biz_ext_info = value
        else:
            self._biz_ext_info = EduTrainExtInfo.from_alipay_dict(value)
    @property
    def first_cate(self):
        return self._first_cate

    @first_cate.setter
    def first_cate(self, value):
        self._first_cate = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rec_ext_info(self):
        return self._rec_ext_info

    @rec_ext_info.setter
    def rec_ext_info(self, value):
        if isinstance(value, EduTrainExtInfo):
            self._rec_ext_info = value
        else:
            self._rec_ext_info = EduTrainExtInfo.from_alipay_dict(value)
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def secend_cate(self):
        return self._secend_cate

    @secend_cate.setter
    def secend_cate(self, value):
        self._secend_cate = value
    @property
    def sub_product_code(self):
        return self._sub_product_code

    @sub_product_code.setter
    def sub_product_code(self, value):
        self._sub_product_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ext_info:
            if hasattr(self.biz_ext_info, 'to_alipay_dict'):
                params['biz_ext_info'] = self.biz_ext_info.to_alipay_dict()
            else:
                params['biz_ext_info'] = self.biz_ext_info
        if self.first_cate:
            if hasattr(self.first_cate, 'to_alipay_dict'):
                params['first_cate'] = self.first_cate.to_alipay_dict()
            else:
                params['first_cate'] = self.first_cate
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rec_ext_info:
            if hasattr(self.rec_ext_info, 'to_alipay_dict'):
                params['rec_ext_info'] = self.rec_ext_info.to_alipay_dict()
            else:
                params['rec_ext_info'] = self.rec_ext_info
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.secend_cate:
            if hasattr(self.secend_cate, 'to_alipay_dict'):
                params['secend_cate'] = self.secend_cate.to_alipay_dict()
            else:
                params['secend_cate'] = self.secend_cate
        if self.sub_product_code:
            if hasattr(self.sub_product_code, 'to_alipay_dict'):
                params['sub_product_code'] = self.sub_product_code.to_alipay_dict()
            else:
                params['sub_product_code'] = self.sub_product_code
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
        o = AlipayCommerceEducateTrainRecommendQueryModel()
        if 'biz_ext_info' in d:
            o.biz_ext_info = d['biz_ext_info']
        if 'first_cate' in d:
            o.first_cate = d['first_cate']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rec_ext_info' in d:
            o.rec_ext_info = d['rec_ext_info']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'secend_cate' in d:
            o.secend_cate = d['secend_cate']
        if 'sub_product_code' in d:
            o.sub_product_code = d['sub_product_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


