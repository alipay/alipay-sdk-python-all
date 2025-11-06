#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopBankCard import ShopBankCard
from alipay.aop.api.domain.AShopBusinessTime import AShopBusinessTime
from alipay.aop.api.domain.ShopContactWayInfo import ShopContactWayInfo
from alipay.aop.api.domain.ShopCertificateInfo import ShopCertificateInfo
from alipay.aop.api.domain.ShopLicenseInfo import ShopLicenseInfo
from alipay.aop.api.domain.ShopProofInfo import ShopProofInfo
from alipay.aop.api.domain.ShopSettleInfo import ShopSettleInfo


class AntMerchantExpandAstoreShopQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAstoreShopQueryResponse, self).__init__()
        self._a_store_id = None
        self._address = None
        self._bank_cards = None
        self._brand_id = None
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
        self._remark = None
        self._settle_infos = None
        self._shop_id = None
        self._shop_type = None
        self._status = None

    @property
    def a_store_id(self):
        return self._a_store_id

    @a_store_id.setter
    def a_store_id(self, value):
        self._a_store_id = value
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
                if isinstance(i, ShopBankCard):
                    self._bank_cards.append(i)
                else:
                    self._bank_cards.append(ShopBankCard.from_alipay_dict(i))
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, AShopBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(AShopBusinessTime.from_alipay_dict(i))
    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, ShopContactWayInfo):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(ShopContactWayInfo.from_alipay_dict(i))
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
        if isinstance(value, ShopCertificateInfo):
            self._legal_info = value
        else:
            self._legal_info = ShopCertificateInfo.from_alipay_dict(value)
    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        if isinstance(value, ShopLicenseInfo):
            self._license_info = value
        else:
            self._license_info = ShopLicenseInfo.from_alipay_dict(value)
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
        if isinstance(value, ShopProofInfo):
            self._proof_info = value
        else:
            self._proof_info = ShopProofInfo.from_alipay_dict(value)
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
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
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAstoreShopQueryResponse, self).parse_response_content(response_content)
        if 'a_store_id' in response:
            self.a_store_id = response['a_store_id']
        if 'address' in response:
            self.address = response['address']
        if 'bank_cards' in response:
            self.bank_cards = response['bank_cards']
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'business_time' in response:
            self.business_time = response['business_time']
        if 'contact_ways' in response:
            self.contact_ways = response['contact_ways']
        if 'digital_poi_id' in response:
            self.digital_poi_id = response['digital_poi_id']
        if 'external_no' in response:
            self.external_no = response['external_no']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'legal_info' in response:
            self.legal_info = response['legal_info']
        if 'license_info' in response:
            self.license_info = response['license_info']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'mcc_l_1' in response:
            self.mcc_l_1 = response['mcc_l_1']
        if 'mcc_l_2' in response:
            self.mcc_l_2 = response['mcc_l_2']
        if 'name' in response:
            self.name = response['name']
        if 'out_door_image' in response:
            self.out_door_image = response['out_door_image']
        if 'proof_info' in response:
            self.proof_info = response['proof_info']
        if 'remark' in response:
            self.remark = response['remark']
        if 'settle_infos' in response:
            self.settle_infos = response['settle_infos']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'shop_type' in response:
            self.shop_type = response['shop_type']
        if 'status' in response:
            self.status = response['status']
