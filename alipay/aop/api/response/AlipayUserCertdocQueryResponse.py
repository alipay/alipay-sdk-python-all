#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayUserCertDocDrivingLicense import AlipayUserCertDocDrivingLicense
from alipay.aop.api.domain.AlipayUserCertDocDrivingLicense import AlipayUserCertDocDrivingLicense
from alipay.aop.api.domain.AlipayUserCertDocIDCard import AlipayUserCertDocIDCard
from alipay.aop.api.domain.AlipayUserCertDocIDCard import AlipayUserCertDocIDCard
from alipay.aop.api.domain.AlipayUserCertDocPassport import AlipayUserCertDocPassport
from alipay.aop.api.domain.AlipayUserCertDocVehicleLicense import AlipayUserCertDocVehicleLicense
from alipay.aop.api.domain.AlipayUserCertDocVehicleLicense import AlipayUserCertDocVehicleLicense


class AlipayUserCertdocQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertdocQueryResponse, self).__init__()
        self._driving_license = None
        self._driving_license_list = None
        self._identity_card = None
        self._identity_card_list = None
        self._passport_list = None
        self._self_vehicle_license_list = None
        self._vehicle_license_list = None

    @property
    def driving_license(self):
        return self._driving_license

    @driving_license.setter
    def driving_license(self, value):
        if isinstance(value, AlipayUserCertDocDrivingLicense):
            self._driving_license = value
        else:
            self._driving_license = AlipayUserCertDocDrivingLicense.from_alipay_dict(value)
    @property
    def driving_license_list(self):
        return self._driving_license_list

    @driving_license_list.setter
    def driving_license_list(self, value):
        if isinstance(value, list):
            self._driving_license_list = list()
            for i in value:
                if isinstance(i, AlipayUserCertDocDrivingLicense):
                    self._driving_license_list.append(i)
                else:
                    self._driving_license_list.append(AlipayUserCertDocDrivingLicense.from_alipay_dict(i))
    @property
    def identity_card(self):
        return self._identity_card

    @identity_card.setter
    def identity_card(self, value):
        if isinstance(value, AlipayUserCertDocIDCard):
            self._identity_card = value
        else:
            self._identity_card = AlipayUserCertDocIDCard.from_alipay_dict(value)
    @property
    def identity_card_list(self):
        return self._identity_card_list

    @identity_card_list.setter
    def identity_card_list(self, value):
        if isinstance(value, list):
            self._identity_card_list = list()
            for i in value:
                if isinstance(i, AlipayUserCertDocIDCard):
                    self._identity_card_list.append(i)
                else:
                    self._identity_card_list.append(AlipayUserCertDocIDCard.from_alipay_dict(i))
    @property
    def passport_list(self):
        return self._passport_list

    @passport_list.setter
    def passport_list(self, value):
        if isinstance(value, list):
            self._passport_list = list()
            for i in value:
                if isinstance(i, AlipayUserCertDocPassport):
                    self._passport_list.append(i)
                else:
                    self._passport_list.append(AlipayUserCertDocPassport.from_alipay_dict(i))
    @property
    def self_vehicle_license_list(self):
        return self._self_vehicle_license_list

    @self_vehicle_license_list.setter
    def self_vehicle_license_list(self, value):
        if isinstance(value, list):
            self._self_vehicle_license_list = list()
            for i in value:
                if isinstance(i, AlipayUserCertDocVehicleLicense):
                    self._self_vehicle_license_list.append(i)
                else:
                    self._self_vehicle_license_list.append(AlipayUserCertDocVehicleLicense.from_alipay_dict(i))
    @property
    def vehicle_license_list(self):
        return self._vehicle_license_list

    @vehicle_license_list.setter
    def vehicle_license_list(self, value):
        if isinstance(value, list):
            self._vehicle_license_list = list()
            for i in value:
                if isinstance(i, AlipayUserCertDocVehicleLicense):
                    self._vehicle_license_list.append(i)
                else:
                    self._vehicle_license_list.append(AlipayUserCertDocVehicleLicense.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertdocQueryResponse, self).parse_response_content(response_content)
        if 'driving_license' in response:
            self.driving_license = response['driving_license']
        if 'driving_license_list' in response:
            self.driving_license_list = response['driving_license_list']
        if 'identity_card' in response:
            self.identity_card = response['identity_card']
        if 'identity_card_list' in response:
            self.identity_card_list = response['identity_card_list']
        if 'passport_list' in response:
            self.passport_list = response['passport_list']
        if 'self_vehicle_license_list' in response:
            self.self_vehicle_license_list = response['self_vehicle_license_list']
        if 'vehicle_license_list' in response:
            self.vehicle_license_list = response['vehicle_license_list']
