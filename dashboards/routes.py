from flask import Blueprint, render_template

dashboards_bp = Blueprint(
    'dashboards_bp',
    __name__,
    template_folder='templates'  # This points to dashboards/templates/
)

@dashboards_bp.route('/buyer/home')
def buyer_home():
    return render_template('buyer_home.html')

@dashboards_bp.route('/supplier/home')
def supplier_home():
    return render_template('supplier_home.html')

@dashboards_bp.route('/admin/home')
def admin_home():
    return render_template('admin_home.html')

@dashboards_bp.route('/supplier/po/acknowledge', methods=['POST'])
def acknowledge_po():
    # Validate PO number, update status, log event
    pass

@dashboards_bp.route('/supplier/po/download', methods=['GET'])
def download_po():
    # Fetch PO PDF, return as file response
    pass
@dashboards_bp.route('/buyer/po/create', methods=['GET', 'POST'])
def create_po():
    # Display form on GET, process form on POST
    pass

