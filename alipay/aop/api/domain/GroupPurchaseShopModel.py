#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupPurchaseBankCard import GroupPurchaseBankCard
from alipay.aop.api.domain.GroupPurchaseBusinessTime import GroupPurchaseBusinessTime
from alipay.aop.api.domain.GroupPurchaseShopContactWayInfo import GroupPurchaseShopContactWayInfo
from alipay.aop.api.domain.GroupPurchaseCertificateInfo import GroupPurchaseCertificateInfo
from alipay.aop.api.domain.GroupPurchaseShopLicenseInfo import GroupPurchaseShopLicenseInfo
from alipay.aop.api.domain.GroupPurchaseProofInfo import GroupPurchaseProofInfo
from alipay.aop.api.domain.GroupPurchaseSettleInfo import GroupPurchaseSettleInfo


class GroupPurchaseShopModel(object):

    def __init__(self):
        self._address = None
        self._bank_cards = None
        self._business_time = None
        self._contact_ways = None
        self._digital_poi_id = None
        self._external_no = None
        self._latitude = None
        self._legal_info = None
        self._license_info = None
        self._longitude = None
        self._mcc_l_1 = None
        self._mcc_l_2 = None
        self._name = None
        self._out_door_image = None
        self._proof_info = None
        self._settle_infos = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bank_cards(self):
        return self._bank_cards

    @bank_cards.setter
    def bank_cards(self, value):
        if isinstance(value, list):
            self._bank_cards = list()
            for i in value:
                if isinstance(i, GroupPurchaseBankCard):
                    self._bank_cards.append(i)
                else:
                    self._bank_cards.append(GroupPurchaseBankCard.from_alipay_dict(i))
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, GroupPurchaseBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(GroupPurchaseBusinessTime.from_alipay_dict(i))
    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, GroupPurchaseShopContactWayInfo):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(GroupPurchaseShopContactWayInfo.from_alipay_dict(i))
    @property
    def digital_poi_id(self):
        return self._digital_poi_id

    @digital_poi_id.setter
    def digital_poi_id(self, value):
        self._digital_poi_id = value
    @property
    def external_no(self):
        return self._external_no

    @external_no.setter
    def external_no(self, value):
        self._external_no = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def legal_info(self):
        return self._legal_info

    @legal_info.setter
    def legal_info(self, value):
        if isinstance(value, GroupPurchaseCertificateInfo):
            self._legal_info = value
        else:
            self._legal_info = GroupPurchaseCertificateInfo.from_alipay_dict(value)
    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        if isinstance(value, GroupPurchaseShopLicenseInfo):
            self._license_info = value
        else:
            self._license_info = GroupPurchaseShopLicenseInfo.from_alipay_dict(value)
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mcc_l_1(self):
        return self._mcc_l_1

    @mcc_l_1.setter
    def mcc_l_1(self, value):
        self._mcc_l_1 = value
    @property
    def mcc_l_2(self):
        return self._mcc_l_2

    @mcc_l_2.setter
    def mcc_l_2(self, value):
        self._mcc_l_2 = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_door_image(self):
        return self._out_door_image

    @out_door_image.setter
    def out_door_image(self, value):
        self._out_door_image = value
    @property
    def proof_info(self):
        return self._proof_info

    @proof_info.setter
    def proof_info(self, value):
        if isinstance(value, GroupPurchaseProofInfo):
            self._proof_info = value
        else:
            self._proof_info = GroupPurchaseProofInfo.from_alipay_dict(value)
    @property
    def settle_infos(self):
        return self._settle_infos

    @settle_infos.setter
    def settle_infos(self, value):
        if isinstance(value, list):
            self._settle_infos = list()
            for i in value:
                if isinstance(i, GroupPurchaseSettleInfo):
                    self._settle_infos.append(i)
                else:
                    self._settle_infos.append(GroupPurchaseSettleInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.bank_cards:
            if isinstance(self.bank_cards, list):
                for i in range(0, len(self.bank_cards)):
                    element = self.bank_cards[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_cards[i] = element.to_alipay_dict()
            if hasattr(self.bank_cards, 'to_alipay_dict'):
                params['bank_cards'] = self.bank_cards.to_alipay_dict()
            else:
                params['bank_cards'] = self.bank_cards
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.contact_ways:
            if isinstance(self.contact_ways, list):
                for i in range(0, len(self.contact_ways)):
                    element = self.contact_ways[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_ways[i] = element.to_alipay_dict()
            if hasattr(self.contact_ways, 'to_alipay_dict'):
                params['contact_ways'] = self.contact_ways.to_alipay_dict()
            else:
                params['contact_ways'] = self.contact_ways
        if self.digital_poi_id:
            if hasattr(self.digital_poi_id, 'to_alipay_dict'):
                params['digital_poi_id'] = self.digital_poi_id.to_alipay_dict()
            else:
                params['digital_poi_id'] = self.digital_poi_id
        if self.external_no:
            if hasattr(self.external_no, 'to_alipay_dict'):
                params['external_no'] = self.external_no.to_alipay_dict()
            else:
                params['external_no'] = self.external_no
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.legal_info:
            if hasattr(self.legal_info, 'to_alipay_dict'):
                params['legal_info'] = self.legal_info.to_alipay_dict()
            else:
                params['legal_info'] = self.legal_info
        if self.license_info:
            if hasattr(self.license_info, 'to_alipay_dict'):
                params['license_info'] = self.license_info.to_alipay_dict()
            else:
                params['license_info'] = self.license_info
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mcc_l_1:
            if hasattr(self.mcc_l_1, 'to_alipay_dict'):
                params['mcc_l_1'] = self.mcc_l_1.to_alipay_dict()
            else:
                params['mcc_l_1'] = self.mcc_l_1
        if self.mcc_l_2:
            if hasattr(self.mcc_l_2, 'to_alipay_dict'):
                params['mcc_l_2'] = self.mcc_l_2.to_alipay_dict()
            else:
                params['mcc_l_2'] = self.mcc_l_2
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_door_image:
            if hasattr(self.out_door_image, 'to_alipay_dict'):
                params['out_door_image'] = self.out_door_image.to_alipay_dict()
            else:
                params['out_door_image'] = self.out_door_image
        if self.proof_info:
            if hasattr(self.proof_info, 'to_alipay_dict'):
                params['proof_info'] = self.proof_info.to_alipay_dict()
            else:
                params['proof_info'] = self.proof_info
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupPurchaseShopModel()
        if 'address' in d:
            o.address = d['address']
        if 'bank_cards' in d:
            o.bank_cards = d['bank_cards']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'contact_ways' in d:
            o.contact_ways = d['contact_ways']
        if 'digital_poi_id' in d:
            o.digital_poi_id = d['digital_poi_id']
        if 'external_no' in d:
            o.external_no = d['external_no']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'legal_info' in d:
            o.legal_info = d['legal_info']
        if 'license_info' in d:
            o.license_info = d['license_info']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mcc_l_1' in d:
            o.mcc_l_1 = d['mcc_l_1']
        if 'mcc_l_2' in d:
            o.mcc_l_2 = d['mcc_l_2']
        if 'name' in d:
            o.name = d['name']
        if 'out_door_image' in d:
            o.out_door_image = d['out_door_image']
        if 'proof_info' in d:
            o.proof_info = d['proof_info']
        if 'settle_infos' in d:
            o.settle_infos = d['settle_infos']
        return o


