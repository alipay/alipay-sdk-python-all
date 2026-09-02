#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentProcurementItemInfoDTO import RentProcurementItemInfoDTO
from alipay.aop.api.domain.RentProcurementReceiverInfoDTO import RentProcurementReceiverInfoDTO


class AlipayCommerceRentProcurementOrderCreateModel(object):

    def __init__(self):
        self._face_activation_strategy = None
        self._item_infos = None
        self._out_procurement_order_id = None
        self._receiver_info = None
        self._relate_rent_order_id = None

    @property
    def face_activation_strategy(self):
        return self._face_activation_strategy

    @face_activation_strategy.setter
    def face_activation_strategy(self, value):
        self._face_activation_strategy = value
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, RentProcurementItemInfoDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(RentProcurementItemInfoDTO.from_alipay_dict(i))
    @property
    def out_procurement_order_id(self):
        return self._out_procurement_order_id

    @out_procurement_order_id.setter
    def out_procurement_order_id(self, value):
        self._out_procurement_order_id = value
    @property
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, value):
        if isinstance(value, RentProcurementReceiverInfoDTO):
            self._receiver_info = value
        else:
            self._receiver_info = RentProcurementReceiverInfoDTO.from_alipay_dict(value)
    @property
    def relate_rent_order_id(self):
        return self._relate_rent_order_id

    @relate_rent_order_id.setter
    def relate_rent_order_id(self, value):
        self._relate_rent_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_activation_strategy:
            if hasattr(self.face_activation_strategy, 'to_alipay_dict'):
                params['face_activation_strategy'] = self.face_activation_strategy.to_alipay_dict()
            else:
                params['face_activation_strategy'] = self.face_activation_strategy
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.out_procurement_order_id:
            if hasattr(self.out_procurement_order_id, 'to_alipay_dict'):
                params['out_procurement_order_id'] = self.out_procurement_order_id.to_alipay_dict()
            else:
                params['out_procurement_order_id'] = self.out_procurement_order_id
        if self.receiver_info:
            if hasattr(self.receiver_info, 'to_alipay_dict'):
                params['receiver_info'] = self.receiver_info.to_alipay_dict()
            else:
                params['receiver_info'] = self.receiver_info
        if self.relate_rent_order_id:
            if hasattr(self.relate_rent_order_id, 'to_alipay_dict'):
                params['relate_rent_order_id'] = self.relate_rent_order_id.to_alipay_dict()
            else:
                params['relate_rent_order_id'] = self.relate_rent_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentProcurementOrderCreateModel()
        if 'face_activation_strategy' in d:
            o.face_activation_strategy = d['face_activation_strategy']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'out_procurement_order_id' in d:
            o.out_procurement_order_id = d['out_procurement_order_id']
        if 'receiver_info' in d:
            o.receiver_info = d['receiver_info']
        if 'relate_rent_order_id' in d:
            o.relate_rent_order_id = d['relate_rent_order_id']
        return o


