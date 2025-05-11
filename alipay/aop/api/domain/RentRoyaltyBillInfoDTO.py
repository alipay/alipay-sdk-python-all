#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentRoyaltyBillDetailDTO import RentRoyaltyBillDetailDTO


class RentRoyaltyBillInfoDTO(object):

    def __init__(self):
        self._biz_order_id = None
        self._invest_name = None
        self._invest_pid = None
        self._out_order_id = None
        self._royalty_detail_list = None
        self._seller_id = None
        self._seller_name = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def invest_name(self):
        return self._invest_name

    @invest_name.setter
    def invest_name(self, value):
        self._invest_name = value
    @property
    def invest_pid(self):
        return self._invest_pid

    @invest_pid.setter
    def invest_pid(self, value):
        self._invest_pid = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def royalty_detail_list(self):
        return self._royalty_detail_list

    @royalty_detail_list.setter
    def royalty_detail_list(self, value):
        if isinstance(value, list):
            self._royalty_detail_list = list()
            for i in value:
                if isinstance(i, RentRoyaltyBillDetailDTO):
                    self._royalty_detail_list.append(i)
                else:
                    self._royalty_detail_list.append(RentRoyaltyBillDetailDTO.from_alipay_dict(i))
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.invest_name:
            if hasattr(self.invest_name, 'to_alipay_dict'):
                params['invest_name'] = self.invest_name.to_alipay_dict()
            else:
                params['invest_name'] = self.invest_name
        if self.invest_pid:
            if hasattr(self.invest_pid, 'to_alipay_dict'):
                params['invest_pid'] = self.invest_pid.to_alipay_dict()
            else:
                params['invest_pid'] = self.invest_pid
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.royalty_detail_list:
            if isinstance(self.royalty_detail_list, list):
                for i in range(0, len(self.royalty_detail_list)):
                    element = self.royalty_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.royalty_detail_list, 'to_alipay_dict'):
                params['royalty_detail_list'] = self.royalty_detail_list.to_alipay_dict()
            else:
                params['royalty_detail_list'] = self.royalty_detail_list
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRoyaltyBillInfoDTO()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'invest_name' in d:
            o.invest_name = d['invest_name']
        if 'invest_pid' in d:
            o.invest_pid = d['invest_pid']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'royalty_detail_list' in d:
            o.royalty_detail_list = d['royalty_detail_list']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        return o


