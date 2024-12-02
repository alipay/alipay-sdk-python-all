#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessItem import BusinessItem
from alipay.aop.api.domain.ParkingLotChargingRuleInfo import ParkingLotChargingRuleInfo
from alipay.aop.api.domain.ParkingLotServiceInfo import ParkingLotServiceInfo


class AlipayEcoMycarParkingParkinglotinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingParkinglotinfoQueryResponse, self).__init__()
        self._address_id = None
        self._agent_id = None
        self._business_isv = None
        self._charging_rule = None
        self._city_id = None
        self._map_poi_address = None
        self._map_poi_name = None
        self._mchnt_id = None
        self._out_parking_id = None
        self._parking_address = None
        self._parking_fee_description = None
        self._parking_fee_description_img = None
        self._parking_id = None
        self._parking_latitude = None
        self._parking_longitude = None
        self._parking_lot_type = None
        self._parking_lot_type_code = None
        self._parking_mobile = None
        self._parking_name = None
        self._parking_poiid = None
        self._pay_type = None
        self._province_id = None
        self._serivce_url = None
        self._service_list = None
        self._shopingmall_id = None
        self._time_out = None

    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def business_isv(self):
        return self._business_isv

    @business_isv.setter
    def business_isv(self, value):
        if isinstance(value, list):
            self._business_isv = list()
            for i in value:
                if isinstance(i, BusinessItem):
                    self._business_isv.append(i)
                else:
                    self._business_isv.append(BusinessItem.from_alipay_dict(i))
    @property
    def charging_rule(self):
        return self._charging_rule

    @charging_rule.setter
    def charging_rule(self, value):
        if isinstance(value, list):
            self._charging_rule = list()
            for i in value:
                if isinstance(i, ParkingLotChargingRuleInfo):
                    self._charging_rule.append(i)
                else:
                    self._charging_rule.append(ParkingLotChargingRuleInfo.from_alipay_dict(i))
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def map_poi_address(self):
        return self._map_poi_address

    @map_poi_address.setter
    def map_poi_address(self, value):
        self._map_poi_address = value
    @property
    def map_poi_name(self):
        return self._map_poi_name

    @map_poi_name.setter
    def map_poi_name(self, value):
        self._map_poi_name = value
    @property
    def mchnt_id(self):
        return self._mchnt_id

    @mchnt_id.setter
    def mchnt_id(self, value):
        self._mchnt_id = value
    @property
    def out_parking_id(self):
        return self._out_parking_id

    @out_parking_id.setter
    def out_parking_id(self, value):
        self._out_parking_id = value
    @property
    def parking_address(self):
        return self._parking_address

    @parking_address.setter
    def parking_address(self, value):
        self._parking_address = value
    @property
    def parking_fee_description(self):
        return self._parking_fee_description

    @parking_fee_description.setter
    def parking_fee_description(self, value):
        self._parking_fee_description = value
    @property
    def parking_fee_description_img(self):
        return self._parking_fee_description_img

    @parking_fee_description_img.setter
    def parking_fee_description_img(self, value):
        self._parking_fee_description_img = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def parking_latitude(self):
        return self._parking_latitude

    @parking_latitude.setter
    def parking_latitude(self, value):
        self._parking_latitude = value
    @property
    def parking_longitude(self):
        return self._parking_longitude

    @parking_longitude.setter
    def parking_longitude(self, value):
        self._parking_longitude = value
    @property
    def parking_lot_type(self):
        return self._parking_lot_type

    @parking_lot_type.setter
    def parking_lot_type(self, value):
        self._parking_lot_type = value
    @property
    def parking_lot_type_code(self):
        return self._parking_lot_type_code

    @parking_lot_type_code.setter
    def parking_lot_type_code(self, value):
        self._parking_lot_type_code = value
    @property
    def parking_mobile(self):
        return self._parking_mobile

    @parking_mobile.setter
    def parking_mobile(self, value):
        self._parking_mobile = value
    @property
    def parking_name(self):
        return self._parking_name

    @parking_name.setter
    def parking_name(self, value):
        self._parking_name = value
    @property
    def parking_poiid(self):
        return self._parking_poiid

    @parking_poiid.setter
    def parking_poiid(self, value):
        self._parking_poiid = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def province_id(self):
        return self._province_id

    @province_id.setter
    def province_id(self, value):
        self._province_id = value
    @property
    def serivce_url(self):
        return self._serivce_url

    @serivce_url.setter
    def serivce_url(self, value):
        self._serivce_url = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                if isinstance(i, ParkingLotServiceInfo):
                    self._service_list.append(i)
                else:
                    self._service_list.append(ParkingLotServiceInfo.from_alipay_dict(i))
    @property
    def shopingmall_id(self):
        return self._shopingmall_id

    @shopingmall_id.setter
    def shopingmall_id(self, value):
        self._shopingmall_id = value
    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, value):
        self._time_out = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingParkinglotinfoQueryResponse, self).parse_response_content(response_content)
        if 'address_id' in response:
            self.address_id = response['address_id']
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'business_isv' in response:
            self.business_isv = response['business_isv']
        if 'charging_rule' in response:
            self.charging_rule = response['charging_rule']
        if 'city_id' in response:
            self.city_id = response['city_id']
        if 'map_poi_address' in response:
            self.map_poi_address = response['map_poi_address']
        if 'map_poi_name' in response:
            self.map_poi_name = response['map_poi_name']
        if 'mchnt_id' in response:
            self.mchnt_id = response['mchnt_id']
        if 'out_parking_id' in response:
            self.out_parking_id = response['out_parking_id']
        if 'parking_address' in response:
            self.parking_address = response['parking_address']
        if 'parking_fee_description' in response:
            self.parking_fee_description = response['parking_fee_description']
        if 'parking_fee_description_img' in response:
            self.parking_fee_description_img = response['parking_fee_description_img']
        if 'parking_id' in response:
            self.parking_id = response['parking_id']
        if 'parking_latitude' in response:
            self.parking_latitude = response['parking_latitude']
        if 'parking_longitude' in response:
            self.parking_longitude = response['parking_longitude']
        if 'parking_lot_type' in response:
            self.parking_lot_type = response['parking_lot_type']
        if 'parking_lot_type_code' in response:
            self.parking_lot_type_code = response['parking_lot_type_code']
        if 'parking_mobile' in response:
            self.parking_mobile = response['parking_mobile']
        if 'parking_name' in response:
            self.parking_name = response['parking_name']
        if 'parking_poiid' in response:
            self.parking_poiid = response['parking_poiid']
        if 'pay_type' in response:
            self.pay_type = response['pay_type']
        if 'province_id' in response:
            self.province_id = response['province_id']
        if 'serivce_url' in response:
            self.serivce_url = response['serivce_url']
        if 'service_list' in response:
            self.service_list = response['service_list']
        if 'shopingmall_id' in response:
            self.shopingmall_id = response['shopingmall_id']
        if 'time_out' in response:
            self.time_out = response['time_out']
