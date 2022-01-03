import sympy as sp
from ipywidgets import interact
from IPython.display import Image, Math, Latex, clear_output, Markdown

def input_matrix():
    """
    Input a matrix. Input number of rows,
    then input each row as a space seperated list of the elements.
    I.e 1 0 0 0 -1 0

    Parameters
    ----------
    None

    Returns
    -------
    A : sympy.matrices.dense.MutableDenseMatrix
        the input matrix
    """
    print("")
    n = int(input("No. Rows: ")) 
    print("Input each row as a space seperated list of the elements.")
    print("E.g: 1 0 0 0 -1 0")
    A = sp.Matrix([])
    # Row wise input
    for i in range(n):
        ith_row = sp.sympify(input("Row {}: ".format(i+1)).split(" "))
        A = A.row_insert(i, sp.Matrix([ith_row]))
    return A


def subs_matrix(p, A):
    """
    Substitute a matrix into a polynomial, by default
    sympy doesn't deal with constants as we would expect,
    so we have to do some hacky sympy expression manipulation.

    Parameters
    ----------
    p : sympy.core.add.Add
        polynomial to sub into

    A : sympy.matrices.dense.MutableDenseMatrix
        the input matrix
    Returns
    -------
    p(A) : sympy.matrices.dense.MutableDenseMatrix
        the substituted matrix
    """
    n = A.shape[0]
    x = sp.symbols('x')
    p = sp.expand(p)
    try:
        const = p.func(*[term for term in p.args if not term.free_symbols])
        return const * sp.eye(n) + (p - const).subs(x, A)
    except TypeError:
        # No constant term
        return p.subs(x, A)


def gram_schmidt():
    """
    Take in a matrix of basis vectors and apply the Gram Schmidt process
    to produce an orthonormalized basis. 
    Displays results. 
    Returns None.
    """
    display(Markdown("------------------------------"))
    display(Markdown("### Input Matrix of Vectors"))
    A = input_matrix()
    display(A)
    display(Markdown("Input Vectors"))
    vlist = [A.col(i) for i in range(A.shape[1])] # Cols of A
    display(vlist)
    display(Markdown("------------------------------"))
    display(Markdown("### Orthonormalized Basis Vectors"))
    display(sp.Matrix.orthogonalize(*vlist, normalize=True))

def interactive_min_poly_finder(A, char_poly):
    """
    Find the minimal polynomial of a matrix.
    Uses ipython widgets to interactively vary the powers of each irreducible
    factor of the minimal polynomial. Displays the result of the f(A), where
    f is the product of the irreducible factors raised to the given powers, n_1, n_2, ...
    The smallest combination of powers such that f(A) is the zero matrix gives
    us the minimal polynomial.
    """
    x = sp.symbols('x')
    n = A.shape[0]
    factor_pairs = sp.factor_list(char_poly)[1]
    factors = [factor_pair[0] for factor_pair in factor_pairs]
    alg_mult = [factor_pair[1] for factor_pair in factor_pairs]
    m = max(alg_mult)
    @interact(n_1=(1,m), n_2=(1,m), n_3=(1,m), n_4=(1,m), n_5=(1,m), n_6=(1,m))
    def interactive_powers(n_1=1, n_2=1, n_3=1, n_4=1, n_5=1, n_6=1):
        substituted_matrix = sp.eye(n) # Initialize
        arg_list = [n_1, n_2, n_3, n_4, n_5, n_6]
        factors_raised = []
        for i in range(len(factors)):
            substituted_matrix *= subs_matrix(factors[i], A)**arg_list[i]
            factors_raised.append(factors[i].subs(x, 'A')**arg_list[i])
        display(factors_raised)
        display(substituted_matrix)


def main(A):
    """Main cell. Cba to properly write a docstring for this."""
    display(Markdown("------------------------------"))
    display(Markdown("### Input Matrix"))
    n = A.shape[0]
    display(A)
    display(Markdown("------------------------------"))
    display(Markdown("### Eigenvectors and Eigenvalues"))
    print("(eigenvalue, algebraic_multiplicity, [eigenvectors])")
    display(A.eigenvects())
    x = sp.symbols('x')
    char_poly = A.charpoly(x).as_expr()
    # print("Characteristic Polynomial Expanded: ", char_poly)
    display(Markdown(f"Characteristic Polynomial Expanded: ${str(char_poly).replace('**', '^').replace('*', '')}$"))
    display(Markdown(f"Characteristic Polynomial Factorized: ${str(sp.factor(char_poly)).replace('**', '^').replace('*', '')}$"))
    # print("Characteristic Polynomial Factorized: ", sp.factor(char_poly))
    # display(sp.factor(char_poly))
    display(Markdown("------------------------------"))
    display(Markdown("### Interactive Minimal Polynomial Finder"))
    display(Markdown("Vary sliders until the zero matrix is produced."))
    display(Markdown("Note: the number of sliders are hard coded so depending on the number of factors, some sliders won't do anything."))
    interactive_min_poly_finder(A, char_poly)
    display(Markdown("------------------------------"))
    display(Markdown("### Jordan Canonical Form"))
    P, J = A.jordan_form()
    display(Markdown("$P^-1 A P = J$"))
    display([P**-1, A, P, J])
    display(Markdown("##### Jordan Basis"))
    display([P.col(i) for i in range(P.shape[1])])
    display(Markdown("------------------------------"))
    display(Markdown("### Ranks of $f_i(A)$"))
    display(Markdown("Where $f_i$ are factors of the minimal poly."))
    display(Markdown("Useful for Rational Canonical Form."))
    factor_pairs = sp.factor_list(char_poly)[1]
    factors = [factor_pair[0] for factor_pair in factor_pairs]
    for factor in factors:
        sub_mat = subs_matrix(factor, A)
        display(Markdown(f"Rank of $({factor.subs(x, 'A')}) = {sub_mat.rank()}$"))

if __name__ == "__main__":
    print("Don't run this file directly. Instead use the ipython notebook file.")
