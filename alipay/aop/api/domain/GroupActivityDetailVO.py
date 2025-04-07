#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CouponActivityContentVO import CouponActivityContentVO
from alipay.aop.api.domain.CustomActivityContentVO import CustomActivityContentVO
from alipay.aop.api.domain.GoodsActivityContentVO import GoodsActivityContentVO


class GroupActivityDetailVO(object):

    def __init__(self):
        self._biz_type = None
        self._client_position = None
        self._coupon_content = None
        self._custom_content = None
        self._gmt_end = None
        self._gmt_start = None
        self._goods_content = None
        self._group_activity_id = None
        self._group_ids = None
        self._priority = None
        self._status = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def client_position(self):
        return self._client_position

    @client_position.setter
    def client_position(self, value):
        self._client_position = value
    @property
    def coupon_content(self):
        return self._coupon_content

    @coupon_content.setter
    def coupon_content(self, value):
        if isinstance(value, CouponActivityContentVO):
            self._coupon_content = value
        else:
            self._coupon_content = CouponActivityContentVO.from_alipay_dict(value)
    @property
    def custom_content(self):
        return self._custom_content

    @custom_content.setter
    def custom_content(self, value):
        if isinstance(value, CustomActivityContentVO):
            self._custom_content = value
        else:
            self._custom_content = CustomActivityContentVO.from_alipay_dict(value)
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def goods_content(self):
        return self._goods_content

    @goods_content.setter
    def goods_content(self, value):
        if isinstance(value, GoodsActivityContentVO):
            self._goods_content = value
        else:
            self._goods_content = GoodsActivityContentVO.from_alipay_dict(value)
    @property
    def group_activity_id(self):
        return self._group_activity_id

    @group_activity_id.setter
    def group_activity_id(self, value):
        self._group_activity_id = value
    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.client_position:
            if hasattr(self.client_position, 'to_alipay_dict'):
                params['client_position'] = self.client_position.to_alipay_dict()
            else:
                params['client_position'] = self.client_position
        if self.coupon_content:
            if hasattr(self.coupon_content, 'to_alipay_dict'):
                params['coupon_content'] = self.coupon_content.to_alipay_dict()
            else:
                params['coupon_content'] = self.coupon_content
        if self.custom_content:
            if hasattr(self.custom_content, 'to_alipay_dict'):
                params['custom_content'] = self.custom_content.to_alipay_dict()
            else:
                params['custom_content'] = self.custom_content
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.goods_content:
            if hasattr(self.goods_content, 'to_alipay_dict'):
                params['goods_content'] = self.goods_content.to_alipay_dict()
            else:
                params['goods_content'] = self.goods_content
        if self.group_activity_id:
            if hasattr(self.group_activity_id, 'to_alipay_dict'):
                params['group_activity_id'] = self.group_activity_id.to_alipay_dict()
            else:
                params['group_activity_id'] = self.group_activity_id
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
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
        o = GroupActivityDetailVO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'client_position' in d:
            o.client_position = d['client_position']
        if 'coupon_content' in d:
            o.coupon_content = d['coupon_content']
        if 'custom_content' in d:
            o.custom_content = d['custom_content']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'goods_content' in d:
            o.goods_content = d['goods_content']
        if 'group_activity_id' in d:
            o.group_activity_id = d['group_activity_id']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'priority' in d:
            o.priority = d['priority']
        if 'status' in d:
            o.status = d['status']
        return o


