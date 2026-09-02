#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentProcurementAdditionalMediaInfoVO import RentProcurementAdditionalMediaInfoVO
from alipay.aop.api.domain.RentProcurementAddressInfoVO import RentProcurementAddressInfoVO
from alipay.aop.api.domain.RentProcurementDeliveryInfoVO import RentProcurementDeliveryInfoVO
from alipay.aop.api.domain.RentProcurementDeviceInfoVO import RentProcurementDeviceInfoVO
from alipay.aop.api.domain.RentProcurementItemInfoVO import RentProcurementItemInfoVO
from alipay.aop.api.domain.RentProcurementPriceInfoVO import RentProcurementPriceInfoVO
from alipay.aop.api.domain.RentProcurementRefundInfoVO import RentProcurementRefundInfoVO


class AlipayCommerceRentProcurementOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentProcurementOrderQueryResponse, self).__init__()
        self._additional_media_info = None
        self._address_info = None
        self._cancel_status = None
        self._delivery_infos = None
        self._device_infos = None
        self._item_infos = None
        self._out_procurement_order_id = None
        self._out_rent_order_id = None
        self._price_info = None
        self._procurement_initiator = None
        self._procurement_order_id = None
        self._refund_info = None
        self._relate_rent_order_id = None
        self._status = None

    @property
    def additional_media_info(self):
        return self._additional_media_info

    @additional_media_info.setter
    def additional_media_info(self, value):
        if isinstance(value, RentProcurementAdditionalMediaInfoVO):
            self._additional_media_info = value
        else:
            self._additional_media_info = RentProcurementAdditionalMediaInfoVO.from_alipay_dict(value)
    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentProcurementAddressInfoVO):
            self._address_info = value
        else:
            self._address_info = RentProcurementAddressInfoVO.from_alipay_dict(value)
    @property
    def cancel_status(self):
        return self._cancel_status

    @cancel_status.setter
    def cancel_status(self, value):
        self._cancel_status = value
    @property
    def delivery_infos(self):
        return self._delivery_infos

    @delivery_infos.setter
    def delivery_infos(self, value):
        if isinstance(value, list):
            self._delivery_infos = list()
            for i in value:
                if isinstance(i, RentProcurementDeliveryInfoVO):
                    self._delivery_infos.append(i)
                else:
                    self._delivery_infos.append(RentProcurementDeliveryInfoVO.from_alipay_dict(i))
    @property
    def device_infos(self):
        return self._device_infos

    @device_infos.setter
    def device_infos(self, value):
        if isinstance(value, list):
            self._device_infos = list()
            for i in value:
                if isinstance(i, RentProcurementDeviceInfoVO):
                    self._device_infos.append(i)
                else:
                    self._device_infos.append(RentProcurementDeviceInfoVO.from_alipay_dict(i))
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, RentProcurementItemInfoVO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(RentProcurementItemInfoVO.from_alipay_dict(i))
    @property
    def out_procurement_order_id(self):
        return self._out_procurement_order_id

    @out_procurement_order_id.setter
    def out_procurement_order_id(self, value):
        self._out_procurement_order_id = value
    @property
    def out_rent_order_id(self):
        return self._out_rent_order_id

    @out_rent_order_id.setter
    def out_rent_order_id(self, value):
        self._out_rent_order_id = value
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, RentProcurementPriceInfoVO):
            self._price_info = value
        else:
            self._price_info = RentProcurementPriceInfoVO.from_alipay_dict(value)
    @property
    def procurement_initiator(self):
        return self._procurement_initiator

    @procurement_initiator.setter
    def procurement_initiator(self, value):
        self._procurement_initiator = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value
    @property
    def refund_info(self):
        return self._refund_info

    @refund_info.setter
    def refund_info(self, value):
        if isinstance(value, RentProcurementRefundInfoVO):
            self._refund_info = value
        else:
            self._refund_info = RentProcurementRefundInfoVO.from_alipay_dict(value)
    @property
    def relate_rent_order_id(self):
        return self._relate_rent_order_id

    @relate_rent_order_id.setter
    def relate_rent_order_id(self, value):
        self._relate_rent_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentProcurementOrderQueryResponse, self).parse_response_content(response_content)
        if 'additional_media_info' in response:
            self.additional_media_info = response['additional_media_info']
        if 'address_info' in response:
            self.address_info = response['address_info']
        if 'cancel_status' in response:
            self.cancel_status = response['cancel_status']
        if 'delivery_infos' in response:
            self.delivery_infos = response['delivery_infos']
        if 'device_infos' in response:
            self.device_infos = response['device_infos']
        if 'item_infos' in response:
            self.item_infos = response['item_infos']
        if 'out_procurement_order_id' in response:
            self.out_procurement_order_id = response['out_procurement_order_id']
        if 'out_rent_order_id' in response:
            self.out_rent_order_id = response['out_rent_order_id']
        if 'price_info' in response:
            self.price_info = response['price_info']
        if 'procurement_initiator' in response:
            self.procurement_initiator = response['procurement_initiator']
        if 'procurement_order_id' in response:
            self.procurement_order_id = response['procurement_order_id']
        if 'refund_info' in response:
            self.refund_info = response['refund_info']
        if 'relate_rent_order_id' in response:
            self.relate_rent_order_id = response['relate_rent_order_id']
        if 'status' in response:
            self.status = response['status']
