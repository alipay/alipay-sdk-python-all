#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PurchaseOrderItemOutDTO(object):

    def __init__(self):
        self._address_ext = None
        self._address_id = None
        self._address_info = None
        self._biz_type = None
        self._category_code = None
        self._category_use = None
        self._currency = None
        self._data_source = None
        self._demander = None
        self._exchange_rate = None
        self._ext_object = None
        self._goods_quotation_id = None
        self._id = None
        self._incoterm = None
        self._invoice_amount = None
        self._is_detail_by_asset_management = None
        self._is_po_by_detail = None
        self._item_description = None
        self._item_name = None
        self._line_num = None
        self._modified_category_code = None
        self._need_by_date_end = None
        self._need_by_date_start = None
        self._order_type = None
        self._origin_tax_amount = None
        self._origin_tax_unit_price = None
        self._pr_item_number = None
        self._pr_number = None
        self._product_id = None
        self._project_number = None
        self._purchase_order_id = None
        self._quantity = None
        self._quantity_received = None
        self._quotation_item_number = None
        self._received = None
        self._receiver = None
        self._sku_id = None
        self._specification = None
        self._sr_number = None
        self._status = None
        self._tax_amount = None
        self._tax_code = None
        self._tax_code_desc = None
        self._tax_rate = None
        self._tax_unit_price = None
        self._uom = None

    @property
    def address_ext(self):
        return self._address_ext

    @address_ext.setter
    def address_ext(self, value):
        self._address_ext = value
    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value
    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        self._address_info = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_use(self):
        return self._category_use

    @category_use.setter
    def category_use(self, value):
        self._category_use = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def demander(self):
        return self._demander

    @demander.setter
    def demander(self, value):
        self._demander = value
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def ext_object(self):
        return self._ext_object

    @ext_object.setter
    def ext_object(self, value):
        self._ext_object = value
    @property
    def goods_quotation_id(self):
        return self._goods_quotation_id

    @goods_quotation_id.setter
    def goods_quotation_id(self, value):
        self._goods_quotation_id = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def incoterm(self):
        return self._incoterm

    @incoterm.setter
    def incoterm(self, value):
        self._incoterm = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def is_detail_by_asset_management(self):
        return self._is_detail_by_asset_management

    @is_detail_by_asset_management.setter
    def is_detail_by_asset_management(self, value):
        self._is_detail_by_asset_management = value
    @property
    def is_po_by_detail(self):
        return self._is_po_by_detail

    @is_po_by_detail.setter
    def is_po_by_detail(self, value):
        self._is_po_by_detail = value
    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        self._item_description = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def line_num(self):
        return self._line_num

    @line_num.setter
    def line_num(self, value):
        self._line_num = value
    @property
    def modified_category_code(self):
        return self._modified_category_code

    @modified_category_code.setter
    def modified_category_code(self, value):
        self._modified_category_code = value
    @property
    def need_by_date_end(self):
        return self._need_by_date_end

    @need_by_date_end.setter
    def need_by_date_end(self, value):
        self._need_by_date_end = value
    @property
    def need_by_date_start(self):
        return self._need_by_date_start

    @need_by_date_start.setter
    def need_by_date_start(self, value):
        self._need_by_date_start = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def origin_tax_amount(self):
        return self._origin_tax_amount

    @origin_tax_amount.setter
    def origin_tax_amount(self, value):
        self._origin_tax_amount = value
    @property
    def origin_tax_unit_price(self):
        return self._origin_tax_unit_price

    @origin_tax_unit_price.setter
    def origin_tax_unit_price(self, value):
        self._origin_tax_unit_price = value
    @property
    def pr_item_number(self):
        return self._pr_item_number

    @pr_item_number.setter
    def pr_item_number(self, value):
        self._pr_item_number = value
    @property
    def pr_number(self):
        return self._pr_number

    @pr_number.setter
    def pr_number(self, value):
        self._pr_number = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def project_number(self):
        return self._project_number

    @project_number.setter
    def project_number(self, value):
        self._project_number = value
    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, value):
        self._purchase_order_id = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_received(self):
        return self._quantity_received

    @quantity_received.setter
    def quantity_received(self, value):
        self._quantity_received = value
    @property
    def quotation_item_number(self):
        return self._quotation_item_number

    @quotation_item_number.setter
    def quotation_item_number(self, value):
        self._quotation_item_number = value
    @property
    def received(self):
        return self._received

    @received.setter
    def received(self, value):
        self._received = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def sr_number(self):
        return self._sr_number

    @sr_number.setter
    def sr_number(self, value):
        self._sr_number = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value
    @property
    def tax_code_desc(self):
        return self._tax_code_desc

    @tax_code_desc.setter
    def tax_code_desc(self, value):
        self._tax_code_desc = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_unit_price(self):
        return self._tax_unit_price

    @tax_unit_price.setter
    def tax_unit_price(self, value):
        self._tax_unit_price = value
    @property
    def uom(self):
        return self._uom

    @uom.setter
    def uom(self, value):
        self._uom = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_ext:
            if hasattr(self.address_ext, 'to_alipay_dict'):
                params['address_ext'] = self.address_ext.to_alipay_dict()
            else:
                params['address_ext'] = self.address_ext
        if self.address_id:
            if hasattr(self.address_id, 'to_alipay_dict'):
                params['address_id'] = self.address_id.to_alipay_dict()
            else:
                params['address_id'] = self.address_id
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_use:
            if hasattr(self.category_use, 'to_alipay_dict'):
                params['category_use'] = self.category_use.to_alipay_dict()
            else:
                params['category_use'] = self.category_use
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.demander:
            if hasattr(self.demander, 'to_alipay_dict'):
                params['demander'] = self.demander.to_alipay_dict()
            else:
                params['demander'] = self.demander
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.ext_object:
            if hasattr(self.ext_object, 'to_alipay_dict'):
                params['ext_object'] = self.ext_object.to_alipay_dict()
            else:
                params['ext_object'] = self.ext_object
        if self.goods_quotation_id:
            if hasattr(self.goods_quotation_id, 'to_alipay_dict'):
                params['goods_quotation_id'] = self.goods_quotation_id.to_alipay_dict()
            else:
                params['goods_quotation_id'] = self.goods_quotation_id
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.incoterm:
            if hasattr(self.incoterm, 'to_alipay_dict'):
                params['incoterm'] = self.incoterm.to_alipay_dict()
            else:
                params['incoterm'] = self.incoterm
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.is_detail_by_asset_management:
            if hasattr(self.is_detail_by_asset_management, 'to_alipay_dict'):
                params['is_detail_by_asset_management'] = self.is_detail_by_asset_management.to_alipay_dict()
            else:
                params['is_detail_by_asset_management'] = self.is_detail_by_asset_management
        if self.is_po_by_detail:
            if hasattr(self.is_po_by_detail, 'to_alipay_dict'):
                params['is_po_by_detail'] = self.is_po_by_detail.to_alipay_dict()
            else:
                params['is_po_by_detail'] = self.is_po_by_detail
        if self.item_description:
            if hasattr(self.item_description, 'to_alipay_dict'):
                params['item_description'] = self.item_description.to_alipay_dict()
            else:
                params['item_description'] = self.item_description
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.line_num:
            if hasattr(self.line_num, 'to_alipay_dict'):
                params['line_num'] = self.line_num.to_alipay_dict()
            else:
                params['line_num'] = self.line_num
        if self.modified_category_code:
            if hasattr(self.modified_category_code, 'to_alipay_dict'):
                params['modified_category_code'] = self.modified_category_code.to_alipay_dict()
            else:
                params['modified_category_code'] = self.modified_category_code
        if self.need_by_date_end:
            if hasattr(self.need_by_date_end, 'to_alipay_dict'):
                params['need_by_date_end'] = self.need_by_date_end.to_alipay_dict()
            else:
                params['need_by_date_end'] = self.need_by_date_end
        if self.need_by_date_start:
            if hasattr(self.need_by_date_start, 'to_alipay_dict'):
                params['need_by_date_start'] = self.need_by_date_start.to_alipay_dict()
            else:
                params['need_by_date_start'] = self.need_by_date_start
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.origin_tax_amount:
            if hasattr(self.origin_tax_amount, 'to_alipay_dict'):
                params['origin_tax_amount'] = self.origin_tax_amount.to_alipay_dict()
            else:
                params['origin_tax_amount'] = self.origin_tax_amount
        if self.origin_tax_unit_price:
            if hasattr(self.origin_tax_unit_price, 'to_alipay_dict'):
                params['origin_tax_unit_price'] = self.origin_tax_unit_price.to_alipay_dict()
            else:
                params['origin_tax_unit_price'] = self.origin_tax_unit_price
        if self.pr_item_number:
            if hasattr(self.pr_item_number, 'to_alipay_dict'):
                params['pr_item_number'] = self.pr_item_number.to_alipay_dict()
            else:
                params['pr_item_number'] = self.pr_item_number
        if self.pr_number:
            if hasattr(self.pr_number, 'to_alipay_dict'):
                params['pr_number'] = self.pr_number.to_alipay_dict()
            else:
                params['pr_number'] = self.pr_number
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.project_number:
            if hasattr(self.project_number, 'to_alipay_dict'):
                params['project_number'] = self.project_number.to_alipay_dict()
            else:
                params['project_number'] = self.project_number
        if self.purchase_order_id:
            if hasattr(self.purchase_order_id, 'to_alipay_dict'):
                params['purchase_order_id'] = self.purchase_order_id.to_alipay_dict()
            else:
                params['purchase_order_id'] = self.purchase_order_id
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quantity_received:
            if hasattr(self.quantity_received, 'to_alipay_dict'):
                params['quantity_received'] = self.quantity_received.to_alipay_dict()
            else:
                params['quantity_received'] = self.quantity_received
        if self.quotation_item_number:
            if hasattr(self.quotation_item_number, 'to_alipay_dict'):
                params['quotation_item_number'] = self.quotation_item_number.to_alipay_dict()
            else:
                params['quotation_item_number'] = self.quotation_item_number
        if self.received:
            if hasattr(self.received, 'to_alipay_dict'):
                params['received'] = self.received.to_alipay_dict()
            else:
                params['received'] = self.received
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.sr_number:
            if hasattr(self.sr_number, 'to_alipay_dict'):
                params['sr_number'] = self.sr_number.to_alipay_dict()
            else:
                params['sr_number'] = self.sr_number
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_code:
            if hasattr(self.tax_code, 'to_alipay_dict'):
                params['tax_code'] = self.tax_code.to_alipay_dict()
            else:
                params['tax_code'] = self.tax_code
        if self.tax_code_desc:
            if hasattr(self.tax_code_desc, 'to_alipay_dict'):
                params['tax_code_desc'] = self.tax_code_desc.to_alipay_dict()
            else:
                params['tax_code_desc'] = self.tax_code_desc
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_unit_price:
            if hasattr(self.tax_unit_price, 'to_alipay_dict'):
                params['tax_unit_price'] = self.tax_unit_price.to_alipay_dict()
            else:
                params['tax_unit_price'] = self.tax_unit_price
        if self.uom:
            if hasattr(self.uom, 'to_alipay_dict'):
                params['uom'] = self.uom.to_alipay_dict()
            else:
                params['uom'] = self.uom
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseOrderItemOutDTO()
        if 'address_ext' in d:
            o.address_ext = d['address_ext']
        if 'address_id' in d:
            o.address_id = d['address_id']
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_use' in d:
            o.category_use = d['category_use']
        if 'currency' in d:
            o.currency = d['currency']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'demander' in d:
            o.demander = d['demander']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'ext_object' in d:
            o.ext_object = d['ext_object']
        if 'goods_quotation_id' in d:
            o.goods_quotation_id = d['goods_quotation_id']
        if 'id' in d:
            o.id = d['id']
        if 'incoterm' in d:
            o.incoterm = d['incoterm']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'is_detail_by_asset_management' in d:
            o.is_detail_by_asset_management = d['is_detail_by_asset_management']
        if 'is_po_by_detail' in d:
            o.is_po_by_detail = d['is_po_by_detail']
        if 'item_description' in d:
            o.item_description = d['item_description']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'line_num' in d:
            o.line_num = d['line_num']
        if 'modified_category_code' in d:
            o.modified_category_code = d['modified_category_code']
        if 'need_by_date_end' in d:
            o.need_by_date_end = d['need_by_date_end']
        if 'need_by_date_start' in d:
            o.need_by_date_start = d['need_by_date_start']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'origin_tax_amount' in d:
            o.origin_tax_amount = d['origin_tax_amount']
        if 'origin_tax_unit_price' in d:
            o.origin_tax_unit_price = d['origin_tax_unit_price']
        if 'pr_item_number' in d:
            o.pr_item_number = d['pr_item_number']
        if 'pr_number' in d:
            o.pr_number = d['pr_number']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'project_number' in d:
            o.project_number = d['project_number']
        if 'purchase_order_id' in d:
            o.purchase_order_id = d['purchase_order_id']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quantity_received' in d:
            o.quantity_received = d['quantity_received']
        if 'quotation_item_number' in d:
            o.quotation_item_number = d['quotation_item_number']
        if 'received' in d:
            o.received = d['received']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'specification' in d:
            o.specification = d['specification']
        if 'sr_number' in d:
            o.sr_number = d['sr_number']
        if 'status' in d:
            o.status = d['status']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_code' in d:
            o.tax_code = d['tax_code']
        if 'tax_code_desc' in d:
            o.tax_code_desc = d['tax_code_desc']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_unit_price' in d:
            o.tax_unit_price = d['tax_unit_price']
        if 'uom' in d:
            o.uom = d['uom']
        return o


