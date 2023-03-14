#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAwardTotalInfoVO import OpenApiAwardTotalInfoVO
from alipay.aop.api.domain.OpenApiUserDetailInfo import OpenApiUserDetailInfo


class OpenApiSkuInfoVO(object):

    def __init__(self):
        self._award_total_info_vo = None
        self._desc = None
        self._max_count = None
        self._name = None
        self._share_desc = None
        self._share_info = None
        self._sku_detail_url = None
        self._sku_get_url = None
        self._sku_id = None
        self._sku_img = None
        self._sku_state = None
        self._sku_type = None

    @property
    def award_total_info_vo(self):
        return self._award_total_info_vo

    @award_total_info_vo.setter
    def award_total_info_vo(self, value):
        if isinstance(value, OpenApiAwardTotalInfoVO):
            self._award_total_info_vo = value
        else:
            self._award_total_info_vo = OpenApiAwardTotalInfoVO.from_alipay_dict(value)
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def share_desc(self):
        return self._share_desc

    @share_desc.setter
    def share_desc(self, value):
        self._share_desc = value
    @property
    def share_info(self):
        return self._share_info

    @share_info.setter
    def share_info(self, value):
        if isinstance(value, list):
            self._share_info = list()
            for i in value:
                if isinstance(i, OpenApiUserDetailInfo):
                    self._share_info.append(i)
                else:
                    self._share_info.append(OpenApiUserDetailInfo.from_alipay_dict(i))
    @property
    def sku_detail_url(self):
        return self._sku_detail_url

    @sku_detail_url.setter
    def sku_detail_url(self, value):
        self._sku_detail_url = value
    @property
    def sku_get_url(self):
        return self._sku_get_url

    @sku_get_url.setter
    def sku_get_url(self, value):
        self._sku_get_url = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_img(self):
        return self._sku_img

    @sku_img.setter
    def sku_img(self, value):
        self._sku_img = value
    @property
    def sku_state(self):
        return self._sku_state

    @sku_state.setter
    def sku_state(self, value):
        self._sku_state = value
    @property
    def sku_type(self):
        return self._sku_type

    @sku_type.setter
    def sku_type(self, value):
        self._sku_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_total_info_vo:
            if hasattr(self.award_total_info_vo, 'to_alipay_dict'):
                params['award_total_info_vo'] = self.award_total_info_vo.to_alipay_dict()
            else:
                params['award_total_info_vo'] = self.award_total_info_vo
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.max_count:
            if hasattr(self.max_count, 'to_alipay_dict'):
                params['max_count'] = self.max_count.to_alipay_dict()
            else:
                params['max_count'] = self.max_count
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.share_desc:
            if hasattr(self.share_desc, 'to_alipay_dict'):
                params['share_desc'] = self.share_desc.to_alipay_dict()
            else:
                params['share_desc'] = self.share_desc
        if self.share_info:
            if isinstance(self.share_info, list):
                for i in range(0, len(self.share_info)):
                    element = self.share_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.share_info[i] = element.to_alipay_dict()
            if hasattr(self.share_info, 'to_alipay_dict'):
                params['share_info'] = self.share_info.to_alipay_dict()
            else:
                params['share_info'] = self.share_info
        if self.sku_detail_url:
            if hasattr(self.sku_detail_url, 'to_alipay_dict'):
                params['sku_detail_url'] = self.sku_detail_url.to_alipay_dict()
            else:
                params['sku_detail_url'] = self.sku_detail_url
        if self.sku_get_url:
            if hasattr(self.sku_get_url, 'to_alipay_dict'):
                params['sku_get_url'] = self.sku_get_url.to_alipay_dict()
            else:
                params['sku_get_url'] = self.sku_get_url
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_img:
            if hasattr(self.sku_img, 'to_alipay_dict'):
                params['sku_img'] = self.sku_img.to_alipay_dict()
            else:
                params['sku_img'] = self.sku_img
        if self.sku_state:
            if hasattr(self.sku_state, 'to_alipay_dict'):
                params['sku_state'] = self.sku_state.to_alipay_dict()
            else:
                params['sku_state'] = self.sku_state
        if self.sku_type:
            if hasattr(self.sku_type, 'to_alipay_dict'):
                params['sku_type'] = self.sku_type.to_alipay_dict()
            else:
                params['sku_type'] = self.sku_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiSkuInfoVO()
        if 'award_total_info_vo' in d:
            o.award_total_info_vo = d['award_total_info_vo']
        if 'desc' in d:
            o.desc = d['desc']
        if 'max_count' in d:
            o.max_count = d['max_count']
        if 'name' in d:
            o.name = d['name']
        if 'share_desc' in d:
            o.share_desc = d['share_desc']
        if 'share_info' in d:
            o.share_info = d['share_info']
        if 'sku_detail_url' in d:
            o.sku_detail_url = d['sku_detail_url']
        if 'sku_get_url' in d:
            o.sku_get_url = d['sku_get_url']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_img' in d:
            o.sku_img = d['sku_img']
        if 'sku_state' in d:
            o.sku_state = d['sku_state']
        if 'sku_type' in d:
            o.sku_type = d['sku_type']
        return o


