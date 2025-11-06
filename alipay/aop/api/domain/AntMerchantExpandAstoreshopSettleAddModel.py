#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopBankCard import ShopBankCard
from alipay.aop.api.domain.ShopSettleInfo import ShopSettleInfo


class AntMerchantExpandAstoreshopSettleAddModel(object):

    def __init__(self):
        self._bank_cards = None
        self._fund_proofs_pic = None
        self._fund_type = None
        self._legal_back_pic = None
        self._legal_front_pic = None
        self._license_pic = None
        self._promise = None
        self._settle_infos = None
        self._shop_id = None

    @property
    def bank_cards(self):
        return self._bank_cards

    @bank_cards.setter
    def bank_cards(self, value):
        if isinstance(value, ShopBankCard):
            self._bank_cards = value
        else:
            self._bank_cards = ShopBankCard.from_alipay_dict(value)
    @property
    def fund_proofs_pic(self):
        return self._fund_proofs_pic

    @fund_proofs_pic.setter
    def fund_proofs_pic(self, value):
        if isinstance(value, list):
            self._fund_proofs_pic = list()
            for i in value:
                self._fund_proofs_pic.append(i)
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def legal_back_pic(self):
        return self._legal_back_pic

    @legal_back_pic.setter
    def legal_back_pic(self, value):
        self._legal_back_pic = value
    @property
    def legal_front_pic(self):
        return self._legal_front_pic

    @legal_front_pic.setter
    def legal_front_pic(self, value):
        self._legal_front_pic = value
    @property
    def license_pic(self):
        return self._license_pic

    @license_pic.setter
    def license_pic(self, value):
        self._license_pic = value
    @property
    def promise(self):
        return self._promise

    @promise.setter
    def promise(self, value):
        self._promise = value
    @property
    def settle_infos(self):
        return self._settle_infos

    @settle_infos.setter
    def settle_infos(self, value):
        if isinstance(value, list):
            self._settle_infos = list()
            for i in value:
                if isinstance(i, ShopSettleInfo):
                    self._settle_infos.append(i)
                else:
                    self._settle_infos.append(ShopSettleInfo.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_cards:
            if hasattr(self.bank_cards, 'to_alipay_dict'):
                params['bank_cards'] = self.bank_cards.to_alipay_dict()
            else:
                params['bank_cards'] = self.bank_cards
        if self.fund_proofs_pic:
            if isinstance(self.fund_proofs_pic, list):
                for i in range(0, len(self.fund_proofs_pic)):
                    element = self.fund_proofs_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_proofs_pic[i] = element.to_alipay_dict()
            if hasattr(self.fund_proofs_pic, 'to_alipay_dict'):
                params['fund_proofs_pic'] = self.fund_proofs_pic.to_alipay_dict()
            else:
                params['fund_proofs_pic'] = self.fund_proofs_pic
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.legal_back_pic:
            if hasattr(self.legal_back_pic, 'to_alipay_dict'):
                params['legal_back_pic'] = self.legal_back_pic.to_alipay_dict()
            else:
                params['legal_back_pic'] = self.legal_back_pic
        if self.legal_front_pic:
            if hasattr(self.legal_front_pic, 'to_alipay_dict'):
                params['legal_front_pic'] = self.legal_front_pic.to_alipay_dict()
            else:
                params['legal_front_pic'] = self.legal_front_pic
        if self.license_pic:
            if hasattr(self.license_pic, 'to_alipay_dict'):
                params['license_pic'] = self.license_pic.to_alipay_dict()
            else:
                params['license_pic'] = self.license_pic
        if self.promise:
            if hasattr(self.promise, 'to_alipay_dict'):
                params['promise'] = self.promise.to_alipay_dict()
            else:
                params['promise'] = self.promise
        if self.settle_infos:
            if isinstance(self.settle_infos, list):
                for i in range(0, len(self.settle_infos)):
                    element = self.settle_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_infos[i] = element.to_alipay_dict()
            if hasattr(self.settle_infos, 'to_alipay_dict'):
                params['settle_infos'] = self.settle_infos.to_alipay_dict()
            else:
                params['settle_infos'] = self.settle_infos
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAstoreshopSettleAddModel()
        if 'bank_cards' in d:
            o.bank_cards = d['bank_cards']
        if 'fund_proofs_pic' in d:
            o.fund_proofs_pic = d['fund_proofs_pic']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'legal_back_pic' in d:
            o.legal_back_pic = d['legal_back_pic']
        if 'legal_front_pic' in d:
            o.legal_front_pic = d['legal_front_pic']
        if 'license_pic' in d:
            o.license_pic = d['license_pic']
        if 'promise' in d:
            o.promise = d['promise']
        if 'settle_infos' in d:
            o.settle_infos = d['settle_infos']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


