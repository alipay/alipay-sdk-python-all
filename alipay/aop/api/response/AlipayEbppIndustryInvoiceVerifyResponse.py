#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvoiceAirplaneItinerary import InvoiceAirplaneItinerary
from alipay.aop.api.domain.InvoiceItemDTO import InvoiceItemDTO
from alipay.aop.api.domain.InvoicePassenger import InvoicePassenger
from alipay.aop.api.domain.InvoiceTrainItinerary import InvoiceTrainItinerary


class AlipayEbppIndustryInvoiceVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryInvoiceVerifyResponse, self).__init__()
        self._airplane_itinerary = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_telephone = None
        self._invoice_amount = None
        self._invoice_amount_without_tax = None
        self._invoice_kind = None
        self._invoice_tax_amount = None
        self._item_list = None
        self._passenger_list = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_name = None
        self._seller_tax_no = None
        self._seller_telephone = None
        self._train_itinerary = None
        self._verify_result_code = None
        self._verify_result_desc = None

    @property
    def airplane_itinerary(self):
        return self._airplane_itinerary

    @airplane_itinerary.setter
    def airplane_itinerary(self, value):
        if isinstance(value, InvoiceAirplaneItinerary):
            self._airplane_itinerary = value
        else:
            self._airplane_itinerary = InvoiceAirplaneItinerary.from_alipay_dict(value)
    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_bank_name(self):
        return self._buyer_bank_name

    @buyer_bank_name.setter
    def buyer_bank_name(self, value):
        self._buyer_bank_name = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def buyer_telephone(self):
        return self._buyer_telephone

    @buyer_telephone.setter
    def buyer_telephone(self, value):
        self._buyer_telephone = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_amount_without_tax(self):
        return self._invoice_amount_without_tax

    @invoice_amount_without_tax.setter
    def invoice_amount_without_tax(self, value):
        self._invoice_amount_without_tax = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_tax_amount(self):
        return self._invoice_tax_amount

    @invoice_tax_amount.setter
    def invoice_tax_amount(self, value):
        self._invoice_tax_amount = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, InvoiceItemDTO):
                    self._item_list.append(i)
                else:
                    self._item_list.append(InvoiceItemDTO.from_alipay_dict(i))
    @property
    def passenger_list(self):
        return self._passenger_list

    @passenger_list.setter
    def passenger_list(self, value):
        if isinstance(value, list):
            self._passenger_list = list()
            for i in value:
                if isinstance(i, InvoicePassenger):
                    self._passenger_list.append(i)
                else:
                    self._passenger_list.append(InvoicePassenger.from_alipay_dict(i))
    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_bank_account(self):
        return self._seller_bank_account

    @seller_bank_account.setter
    def seller_bank_account(self, value):
        self._seller_bank_account = value
    @property
    def seller_bank_name(self):
        return self._seller_bank_name

    @seller_bank_name.setter
    def seller_bank_name(self, value):
        self._seller_bank_name = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def seller_telephone(self):
        return self._seller_telephone

    @seller_telephone.setter
    def seller_telephone(self, value):
        self._seller_telephone = value
    @property
    def train_itinerary(self):
        return self._train_itinerary

    @train_itinerary.setter
    def train_itinerary(self, value):
        if isinstance(value, InvoiceTrainItinerary):
            self._train_itinerary = value
        else:
            self._train_itinerary = InvoiceTrainItinerary.from_alipay_dict(value)
    @property
    def verify_result_code(self):
        return self._verify_result_code

    @verify_result_code.setter
    def verify_result_code(self, value):
        self._verify_result_code = value
    @property
    def verify_result_desc(self):
        return self._verify_result_desc

    @verify_result_desc.setter
    def verify_result_desc(self, value):
        self._verify_result_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryInvoiceVerifyResponse, self).parse_response_content(response_content)
        if 'airplane_itinerary' in response:
            self.airplane_itinerary = response['airplane_itinerary']
        if 'buyer_address' in response:
            self.buyer_address = response['buyer_address']
        if 'buyer_bank_account' in response:
            self.buyer_bank_account = response['buyer_bank_account']
        if 'buyer_bank_name' in response:
            self.buyer_bank_name = response['buyer_bank_name']
        if 'buyer_name' in response:
            self.buyer_name = response['buyer_name']
        if 'buyer_tax_no' in response:
            self.buyer_tax_no = response['buyer_tax_no']
        if 'buyer_telephone' in response:
            self.buyer_telephone = response['buyer_telephone']
        if 'invoice_amount' in response:
            self.invoice_amount = response['invoice_amount']
        if 'invoice_amount_without_tax' in response:
            self.invoice_amount_without_tax = response['invoice_amount_without_tax']
        if 'invoice_kind' in response:
            self.invoice_kind = response['invoice_kind']
        if 'invoice_tax_amount' in response:
            self.invoice_tax_amount = response['invoice_tax_amount']
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'passenger_list' in response:
            self.passenger_list = response['passenger_list']
        if 'seller_address' in response:
            self.seller_address = response['seller_address']
        if 'seller_bank_account' in response:
            self.seller_bank_account = response['seller_bank_account']
        if 'seller_bank_name' in response:
            self.seller_bank_name = response['seller_bank_name']
        if 'seller_name' in response:
            self.seller_name = response['seller_name']
        if 'seller_tax_no' in response:
            self.seller_tax_no = response['seller_tax_no']
        if 'seller_telephone' in response:
            self.seller_telephone = response['seller_telephone']
        if 'train_itinerary' in response:
            self.train_itinerary = response['train_itinerary']
        if 'verify_result_code' in response:
            self.verify_result_code = response['verify_result_code']
        if 'verify_result_desc' in response:
            self.verify_result_desc = response['verify_result_desc']
