#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantSiteInfo import MerchantSiteInfo


class AlipayOverseasSecondmerchantMaintainQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasSecondmerchantMaintainQuerystatusResponse, self).__init__()
        self._contact_email = None
        self._contact_no = None
        self._cs_email = None
        self._cs_no = None
        self._external_storefront_photo = None
        self._internal_store_photo = None
        self._partner_id = None
        self._payment_method = None
        self._register_address = None
        self._register_country = None
        self._registration_no = None
        self._reject_reason = None
        self._representative_id = None
        self._representative_name = None
        self._secondary_merchant_id = None
        self._secondary_merchant_industry = None
        self._secondary_merchant_name = None
        self._secondary_merchant_type = None
        self._settlement_no = None
        self._shareholder_id = None
        self._shareholder_name = None
        self._site_infos = None
        self._status = None
        self._store_address = None
        self._store_country = None
        self._store_id = None
        self._store_industry = None
        self._store_name = None
        self._store_status = None

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_no(self):
        return self._contact_no

    @contact_no.setter
    def contact_no(self, value):
        self._contact_no = value
    @property
    def cs_email(self):
        return self._cs_email

    @cs_email.setter
    def cs_email(self, value):
        self._cs_email = value
    @property
    def cs_no(self):
        return self._cs_no

    @cs_no.setter
    def cs_no(self, value):
        self._cs_no = value
    @property
    def external_storefront_photo(self):
        return self._external_storefront_photo

    @external_storefront_photo.setter
    def external_storefront_photo(self, value):
        self._external_storefront_photo = value
    @property
    def internal_store_photo(self):
        return self._internal_store_photo

    @internal_store_photo.setter
    def internal_store_photo(self, value):
        self._internal_store_photo = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def register_address(self):
        return self._register_address

    @register_address.setter
    def register_address(self, value):
        self._register_address = value
    @property
    def register_country(self):
        return self._register_country

    @register_country.setter
    def register_country(self, value):
        self._register_country = value
    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def representative_id(self):
        return self._representative_id

    @representative_id.setter
    def representative_id(self, value):
        self._representative_id = value
    @property
    def representative_name(self):
        return self._representative_name

    @representative_name.setter
    def representative_name(self, value):
        self._representative_name = value
    @property
    def secondary_merchant_id(self):
        return self._secondary_merchant_id

    @secondary_merchant_id.setter
    def secondary_merchant_id(self, value):
        self._secondary_merchant_id = value
    @property
    def secondary_merchant_industry(self):
        return self._secondary_merchant_industry

    @secondary_merchant_industry.setter
    def secondary_merchant_industry(self, value):
        self._secondary_merchant_industry = value
    @property
    def secondary_merchant_name(self):
        return self._secondary_merchant_name

    @secondary_merchant_name.setter
    def secondary_merchant_name(self, value):
        self._secondary_merchant_name = value
    @property
    def secondary_merchant_type(self):
        return self._secondary_merchant_type

    @secondary_merchant_type.setter
    def secondary_merchant_type(self, value):
        self._secondary_merchant_type = value
    @property
    def settlement_no(self):
        return self._settlement_no

    @settlement_no.setter
    def settlement_no(self, value):
        self._settlement_no = value
    @property
    def shareholder_id(self):
        return self._shareholder_id

    @shareholder_id.setter
    def shareholder_id(self, value):
        self._shareholder_id = value
    @property
    def shareholder_name(self):
        return self._shareholder_name

    @shareholder_name.setter
    def shareholder_name(self, value):
        self._shareholder_name = value
    @property
    def site_infos(self):
        return self._site_infos

    @site_infos.setter
    def site_infos(self, value):
        if isinstance(value, list):
            self._site_infos = list()
            for i in value:
                if isinstance(i, MerchantSiteInfo):
                    self._site_infos.append(i)
                else:
                    self._site_infos.append(MerchantSiteInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_country(self):
        return self._store_country

    @store_country.setter
    def store_country(self, value):
        self._store_country = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_industry(self):
        return self._store_industry

    @store_industry.setter
    def store_industry(self, value):
        self._store_industry = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_status(self):
        return self._store_status

    @store_status.setter
    def store_status(self, value):
        self._store_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasSecondmerchantMaintainQuerystatusResponse, self).parse_response_content(response_content)
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_no' in response:
            self.contact_no = response['contact_no']
        if 'cs_email' in response:
            self.cs_email = response['cs_email']
        if 'cs_no' in response:
            self.cs_no = response['cs_no']
        if 'external_storefront_photo' in response:
            self.external_storefront_photo = response['external_storefront_photo']
        if 'internal_store_photo' in response:
            self.internal_store_photo = response['internal_store_photo']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'payment_method' in response:
            self.payment_method = response['payment_method']
        if 'register_address' in response:
            self.register_address = response['register_address']
        if 'register_country' in response:
            self.register_country = response['register_country']
        if 'registration_no' in response:
            self.registration_no = response['registration_no']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'representative_id' in response:
            self.representative_id = response['representative_id']
        if 'representative_name' in response:
            self.representative_name = response['representative_name']
        if 'secondary_merchant_id' in response:
            self.secondary_merchant_id = response['secondary_merchant_id']
        if 'secondary_merchant_industry' in response:
            self.secondary_merchant_industry = response['secondary_merchant_industry']
        if 'secondary_merchant_name' in response:
            self.secondary_merchant_name = response['secondary_merchant_name']
        if 'secondary_merchant_type' in response:
            self.secondary_merchant_type = response['secondary_merchant_type']
        if 'settlement_no' in response:
            self.settlement_no = response['settlement_no']
        if 'shareholder_id' in response:
            self.shareholder_id = response['shareholder_id']
        if 'shareholder_name' in response:
            self.shareholder_name = response['shareholder_name']
        if 'site_infos' in response:
            self.site_infos = response['site_infos']
        if 'status' in response:
            self.status = response['status']
        if 'store_address' in response:
            self.store_address = response['store_address']
        if 'store_country' in response:
            self.store_country = response['store_country']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'store_industry' in response:
            self.store_industry = response['store_industry']
        if 'store_name' in response:
            self.store_name = response['store_name']
        if 'store_status' in response:
            self.store_status = response['store_status']
