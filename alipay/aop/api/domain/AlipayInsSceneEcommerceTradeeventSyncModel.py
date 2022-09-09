#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.InsureCertificateDTO import InsureCertificateDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommerceTradeeventSyncModel(object):

    def __init__(self):
        self._buyer = None
        self._event_type = None
        self._insure_certificates = None
        self._item = None
        self._order_dto = None
        self._partner_org_id = None
        self._seller = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, EcomBuyerDTO):
            self._buyer = value
        else:
            self._buyer = EcomBuyerDTO.from_alipay_dict(value)
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def insure_certificates(self):
        return self._insure_certificates

    @insure_certificates.setter
    def insure_certificates(self, value):
        if isinstance(value, list):
            self._insure_certificates = list()
            for i in value:
                if isinstance(i, InsureCertificateDTO):
                    self._insure_certificates.append(i)
                else:
                    self._insure_certificates.append(InsureCertificateDTO.from_alipay_dict(i))
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, EcomItemDTO):
            self._item = value
        else:
            self._item = EcomItemDTO.from_alipay_dict(value)
    @property
    def order_dto(self):
        return self._order_dto

    @order_dto.setter
    def order_dto(self, value):
        if isinstance(value, EcomOrderDTO):
            self._order_dto = value
        else:
            self._order_dto = EcomOrderDTO.from_alipay_dict(value)
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, EcomSellerDTO):
            self._seller = value
        else:
            self._seller = EcomSellerDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.insure_certificates:
            if isinstance(self.insure_certificates, list):
                for i in range(0, len(self.insure_certificates)):
                    element = self.insure_certificates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insure_certificates[i] = element.to_alipay_dict()
            if hasattr(self.insure_certificates, 'to_alipay_dict'):
                params['insure_certificates'] = self.insure_certificates.to_alipay_dict()
            else:
                params['insure_certificates'] = self.insure_certificates
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.order_dto:
            if hasattr(self.order_dto, 'to_alipay_dict'):
                params['order_dto'] = self.order_dto.to_alipay_dict()
            else:
                params['order_dto'] = self.order_dto
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEcommerceTradeeventSyncModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'insure_certificates' in d:
            o.insure_certificates = d['insure_certificates']
        if 'item' in d:
            o.item = d['item']
        if 'order_dto' in d:
            o.order_dto = d['order_dto']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'seller' in d:
            o.seller = d['seller']
        return o


